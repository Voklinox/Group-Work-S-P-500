"""Automated PDF and LaTeX Exporter for S&P 500 Quantitative Data Analysis Project.

Converts all course deliverables from Markdown into:
1. Academic publication-grade PDF files via Pandoc and Typst.
2. Standalone, compilable LaTeX source (.tex) files via Pandoc.
"""

import re
import subprocess
import sys
from pathlib import Path


def export_documents():
    project_root = Path(__file__).resolve().parent.parent
    docs_dir = project_root / "docs"
    pdf_dir = docs_dir / "pdf"
    latex_dir = docs_dir / "latex"

    pdf_dir.mkdir(parents=True, exist_ok=True)
    latex_dir.mkdir(parents=True, exist_ok=True)

    # All project markdown documents in docs/
    md_files = sorted(list(docs_dir.glob("*.md")))

    print(f"Found {len(md_files)} markdown documents in {docs_dir}:")
    for f in md_files:
        print(f"  - {f.name}")

    results = []

    for md_path in md_files:
        base_name = md_path.stem
        tex_path = latex_dir / f"{base_name}.tex"
        pdf_path = pdf_dir / f"{base_name}.pdf"

        print(f"\nProcessing: {md_path.name}")

        # 1. Generate LaTeX .tex file
        cmd_tex = [
            "pandoc",
            str(md_path),
            "-s",
            "--resource-path=.:docs:figures",
            "-o",
            str(tex_path),
        ]
        res_tex = subprocess.run(
            cmd_tex, cwd=str(project_root), capture_output=True, text=True
        )
        if res_tex.returncode != 0:
            print(f"  [ERROR] LaTeX generation failed: {res_tex.stderr}")
            results.append((base_name, "LaTeX", False, res_tex.stderr))
        else:
            tex_size_kb = tex_path.stat().st_size / 1024
            print(f"  [OK] LaTeX: {tex_path.name} ({tex_size_kb:.1f} KB)")
            results.append((base_name, "LaTeX", True, f"{tex_size_kb:.1f} KB"))

        # 2. Prepare cleaned Markdown for Typst PDF (strip internal anchor links)
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        clean_content = re.sub(r"\[(.*?)\]\(#.*?\)", r"\1", content)
        temp_md = project_root / f"_temp_{base_name}.md"
        with open(temp_md, "w", encoding="utf-8") as f:
            f.write(clean_content)

        # 3. Generate PDF via Typst
        cmd_pdf = [
            "pandoc",
            str(temp_md),
            "--pdf-engine=typst",
            "--resource-path=.:docs:figures",
            "-V",
            "papersize=a4",
            "-V",
            "margin-x=2cm",
            "-V",
            "margin-y=2.5cm",
            "-o",
            str(pdf_path),
        ]
        res_pdf = subprocess.run(
            cmd_pdf, cwd=str(project_root), capture_output=True, text=True
        )

        if temp_md.exists():
            temp_md.unlink()

        if res_pdf.returncode != 0:
            print(f"  [ERROR] PDF generation failed: {res_pdf.stderr}")
            results.append((base_name, "PDF", False, res_pdf.stderr))
        else:
            pdf_size_kb = pdf_path.stat().st_size / 1024
            print(f"  [OK] PDF: {pdf_path.name} ({pdf_size_kb:.1f} KB)")
            results.append((base_name, "PDF", True, f"{pdf_size_kb:.1f} KB"))

    print("\n" + "=" * 60)
    print("CONVERSION SUMMARY")
    print("=" * 60)
    all_success = True
    for name, doc_type, success, detail in results:
        status = "PASSED" if success else "FAILED"
        if not success:
            all_success = False
        print(f"{name:<35} | {doc_type:<6} | {status:<6} | {detail}")

    if all_success:
        print("\nAll deliverables converted successfully to PDF and LaTeX!")
        return 0
    else:
        print("\nSome deliverables failed to convert.")
        return 1


if __name__ == "__main__":
    sys.exit(export_documents())

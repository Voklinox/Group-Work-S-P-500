"""Convertit les graphiques Jamovi exportés en PDF vectoriel (outputs/jamovi_export/figures_pdf)
en PNG 300 dpi (outputs/jamovi_export/figures_png), prêts pour le Google Doc.

Les PDF viennent de Jamovi : clic droit sur un graphique → Image → Export (format PDF).
Usage : .venv/bin/python -m src.convert_jamovi_figures   (nécessite pymupdf)
"""
import pathlib

import fitz

SRC = pathlib.Path("outputs/jamovi_export/figures_pdf")
DST = pathlib.Path("outputs/jamovi_export/figures_png")


def main():
    DST.mkdir(parents=True, exist_ok=True)
    for pdf in sorted(SRC.glob("*.pdf")):
        pix = fitz.open(pdf)[0].get_pixmap(dpi=300, alpha=False)
        pix.save(DST / f"{pdf.stem}.png")
        print(pdf.stem, pix.width, pix.height)


if __name__ == "__main__":
    main()

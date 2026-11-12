"""Rend chaque tableau de la sortie Jamovi (index.html du .omv) en PNG 900 dpi-équivalent (x3).

Les tableaux sont des <table> HTML autonomes (styles en ligne). On les rend avec Google Chrome
sans fenêtre (le moteur de rendu de Jamovi), puis on recadre automatiquement les marges blanches.
Usage : .venv/bin/python -m src.render_jamovi_tables
"""
import html, pathlib, re, subprocess, tempfile, zipfile

from PIL import Image, ImageChops

OMV = pathlib.Path("data/processed/sp500_2025.omv")
OUT = pathlib.Path("outputs/jamovi_export/tables_png")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
COMPACT = {8, 9}  # tableaux très larges : marges de cellules réduites pour rester lisibles dans le rapport
COMPACT_CSS = "<style>td,th{padding-left:4px!important;padding-right:7px!important}th{white-space:normal}</style>"
PAGE = ('<!doctype html><meta charset="utf-8"><body style="margin:0;padding:12px;'
        'font-family:Helvetica,Arial,sans-serif;font-size:12px;color:#333;background:#fff;'
        'display:inline-block">{}</body>')


def tables(index_html: str):
    body = index_html[index_html.index("<body"):]
    return re.findall(r"<table.*?</table>", body, flags=re.S)


def caption(tbl: str) -> str:
    m = re.search(r'<span id="label-\d+"[^>]*>(.*?)</span>', tbl, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else ""


def autocrop(path: pathlib.Path, pad: int = 24):
    im = Image.open(path).convert("RGB")
    bbox = ImageChops.difference(im, Image.new("RGB", im.size, "white")).getbbox()
    x0, y0, x1, y1 = bbox
    im.crop((max(0, x0 - pad), max(0, y0 - pad), min(im.width, x1 + pad), min(im.height, y1 + pad))).save(path)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.png"):
        old.unlink()
    idx = zipfile.ZipFile(OMV).read("index.html").decode()
    with tempfile.TemporaryDirectory() as tmp:
        for k, t in enumerate(tables(idx), 1):
            cap = caption(t)
            slug = re.sub(r"[^a-z0-9]+", "_", cap.lower()).strip("_")[:40] or "table"
            src = pathlib.Path(tmp) / f"t{k:02d}.html"
            src.write_text(PAGE.format((COMPACT_CSS if k in COMPACT else "") + t), encoding="utf-8")
            out = OUT / f"t{k:02d}_{slug}.png"
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                            "--force-device-scale-factor=3", "--window-size=1400,1800",
                            f"--screenshot={out}", src.as_uri()],
                           check=True, capture_output=True)
            autocrop(out)
            print(f"t{k:02d}", cap)


if __name__ == "__main__":
    main()

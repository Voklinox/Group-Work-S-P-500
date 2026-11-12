"""Write the plain text of a cached proxy to stdout. Usage: python3 -m src.governance_text <cik> <accession>"""
import sys
from src.collect import ROOT
from src.documents import html_text


def main(argv):
    cik, accession = argv
    print(html_text(ROOT / f"data/raw/governance/{cik}_{accession}.htm"))


if __name__ == "__main__":
    main(sys.argv[1:])

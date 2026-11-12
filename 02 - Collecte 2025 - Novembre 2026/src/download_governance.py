"""Cache every candidate proxy / information statement listed in governance_proxy_candidates.csv.

Single process, at most four request starts per second (src.documents). Refusals are logged in the
download manifest and reported here; nothing is retried around them.
"""
import csv, json
from src.collect import ROOT
from src.documents import fetch


def main():
    rows = list(csv.DictReader((ROOT / "data/reference/governance_proxy_candidates.csv").open()))
    failures = []
    for i, r in enumerate(rows, 1):
        try:
            fetch(r["source_url"], f"data/raw/governance/{r['cik']}_{r['accession']}.htm")
        except Exception as e:
            failures.append(dict(cik=r["cik"], accession=r["accession"], url=r["source_url"], error=str(e)))
        if i % 50 == 0 or i == len(rows):
            print(f"{i}/{len(rows)} cached; failures={len(failures)}", flush=True)
    (ROOT / "outputs/governance_download_failures.json").write_text(json.dumps(failures, indent=2))


if __name__ == "__main__":
    main()

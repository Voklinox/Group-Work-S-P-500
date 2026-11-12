"""F08: check a random sample of annual reports against the table cells (revenue, net income, assets).

A cell counts as 'found' when its value, written in dollars, thousands, millions (0 or 1 decimal) or
billions (1-2 decimals), appears in the report text. 'not_found' cells are read by hand.
Usage: SEC_CONTACT_EMAIL=... python3 -m src.report_sample [N] [seed]   -> data/reference/report_sample_check.csv
"""
import csv, random, re, sys
from src.collect import ROOT, dump_csv
from src.documents import fetch, html_text

VARS = ("revenue_usd", "net_income_usd", "assets_usd")


def forms(v):
    v = abs(v)
    out = {f"{v:,.0f}", f"{v/1e3:,.0f}", f"{v/1e6:,.0f}", f"{v/1e6:,.1f}", f"{v/1e9:,.1f}", f"{v/1e9:,.2f}"}
    return {x for x in out if len(x) >= 4 or "." in x}


def main(n=25, seed=2026):
    rows = [r for r in csv.DictReader((ROOT / "data/processed/financials_2025_WORKING.csv").open()) if r["accession"]]
    sample = random.Random(seed).sample(rows, n)
    out = []
    for r in sample:
        try:
            text = html_text(fetch(r["report_url"], f"data/raw/reports/{r['cik']}_{r['accession']}.htm"))
        except Exception as e:
            out.append(dict(cik=r["cik"], company=r["company"], variable="(document)", value="", status=f"download_failed: {e}"))
            continue
        for v in VARS:
            if not r[v]:
                continue
            ok = any(re.search(r"(?<![\d,.])" + re.escape(f) + r"(?![\d])", text) for f in forms(float(r[v])))
            out.append(dict(cik=r["cik"], company=r["company"], variable=v, value=r[v], status="found" if ok else "not_found"))
    dump_csv(ROOT / "data/reference/report_sample_check.csv", out, ["cik", "company", "variable", "value", "status"])
    from collections import Counter
    print(len(sample), "reports;", dict(Counter(o["status"].split(":")[0] for o in out)))
    for o in out:
        if o["status"] != "found":
            print("  ", o["company"], o["variable"], o["value"], o["status"][:60])


if __name__ == "__main__":
    main(*(int(a) for a in sys.argv[1:]))

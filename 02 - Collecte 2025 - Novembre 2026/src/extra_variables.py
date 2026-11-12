"""Prior-year revenue from the SAME annual filing, for revenue growth (DEC25).

Growth is computed only when the selected revenue is a plain standard concept and the same filing reports
the same concept for the preceding fiscal year (330-385 days, ending 330-400 days earlier). No imputation.
Output: data/reference/revenue_growth_evidence.csv
"""
import csv, json
from datetime import date
from src.collect import ROOT, dump_csv


def prior_revenue(data, namespace, tag, accession, start, end):
    concept = data.get("facts", {}).get(namespace, {}).get(tag)
    if not concept:
        return None
    s, e = date.fromisoformat(start), date.fromisoformat(end)
    values = {}
    for f in concept.get("units", {}).get("USD", []):
        if f.get("accn") != accession or not f.get("start"):
            continue
        fs, fe = date.fromisoformat(f["start"]), date.fromisoformat(f["end"])
        if 330 <= (fe - fs).days <= 385 and 330 <= (e - fe).days <= 400:
            values[(f["start"], f["end"])] = f["val"]
    if len({v for v in values.values()}) != 1:
        return None
    (ps, pe), v = next(iter(values.items()))
    return ps, pe, v


def main():
    fin = list(csv.DictReader((ROOT / "data/processed/financials_2025_WORKING.csv").open()))
    rev = {e["cik"]: e for e in json.loads((ROOT / "data/reference/financial_evidence.json").read_text()) if e["variable"] == "revenue_usd"}
    out = []
    for r in fin:
        e = rev.get(r["cik"])
        if not e or e["namespace"] in ("reviewed", "computed") or ":" in e["tag"]:
            continue
        data = json.loads((ROOT / f"data/raw/sec/CIK{r['cik']}.json").read_text())
        p = prior_revenue(data, e["namespace"], e["tag"], r["accession"], r["period_start"], r["period_end"])
        if p and p[2] > 0 and e["value"] > 0:
            out.append(dict(cik=r["cik"], company=r["company"], tag=e["tag"], accession=r["accession"], current_start=r["period_start"], current_end=r["period_end"],
                            current_value=e["value"], prior_start=p[0], prior_end=p[1], prior_value=p[2], revenue_growth_pct=100 * (e["value"] / p[2] - 1)))
    dump_csv(ROOT / "data/reference/revenue_growth_evidence.csv", out, list(out[0]))
    g = sorted(o["revenue_growth_pct"] for o in out)
    print(len(out), "growth values; min/median/max", round(g[0], 1), round(g[len(g) // 2], 1), round(g[-1], 1))


if __name__ == "__main__":
    main()

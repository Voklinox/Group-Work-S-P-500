"""Screen the working financial table for values to review (F08-F09). Nothing is modified or removed.

Writes data/quarantine/financial_screening.csv (one row per flag) and outputs/financial_screening_summary.json.
Flags: negative equity, negative revenue/assets, margin or ROA outside plausible range, IQR outliers (3x IQR),
financial-sector revenue vs assets, liabilities+equity vs assets mismatch, missing core variables.
"""
import csv, json, statistics
from src.collect import ROOT, dump_csv

FIN = {"Financials"}


def q(values, p):
    v = sorted(values)
    k = (len(v) - 1) * p
    f = int(k)
    return v[f] + (v[min(f + 1, len(v) - 1)] - v[f]) * (k - f)


def main():
    rows = list(csv.DictReader((ROOT / "data/processed/financials_2025_WORKING.csv").open()))
    num = lambda r, c: float(r[c]) if r[c] != "" else None
    flags, summary = [], {}
    for col in ("revenue_usd", "net_income_usd", "assets_usd", "equity_usd", "net_margin_pct", "roa_pct"):
        vals = [num(r, col) for r in rows if num(r, col) is not None]
        q1, q3 = q(vals, .25), q(vals, .75)
        lo, hi = q1 - 3 * (q3 - q1), q3 + 3 * (q3 - q1)
        summary[col] = dict(n=len(vals), missing=len(rows) - len(vals), min=min(vals), median=statistics.median(vals), max=max(vals), iqr_fence=[lo, hi])
        for r in rows:
            v = num(r, col)
            if v is not None and col in ("net_margin_pct", "roa_pct") and (v < lo or v > hi):
                flags.append(dict(cik=r["cik"], company=r["company"], sector=r["sector"], flag=f"{col}_iqr_outlier", value=round(v, 2), detail=f"fence {lo:.1f} to {hi:.1f}"))
    for r in rows:
        rev, ni, a, e, l = (num(r, c) for c in ("revenue_usd", "net_income_usd", "assets_usd", "equity_usd", "liabilities_usd"))
        m, roa = num(r, "net_margin_pct"), num(r, "roa_pct")
        if e is not None and e < 0: flags.append(dict(cik=r["cik"], company=r["company"], sector=r["sector"], flag="negative_equity", value=e, detail="kept; interpret ROE-type ratios with care"))
        if m is not None and (m < -100 or m > 100): flags.append(dict(cik=r["cik"], company=r["company"], sector=r["sector"], flag="margin_beyond_100pct", value=round(m, 1), detail=f"revenue {rev}, net income {ni}"))
        if roa is not None and abs(roa) > 40: flags.append(dict(cik=r["cik"], company=r["company"], sector=r["sector"], flag="roa_beyond_40pct", value=round(roa, 1), detail=f"net income {ni}, assets {a}"))
        if rev is not None and rev < 0: flags.append(dict(cik=r["cik"], company=r["company"], sector=r["sector"], flag="negative_revenue", value=rev, detail=""))
        if a is not None and e is not None and l is not None and abs(a - e - l) > 0.05 * a:
            flags.append(dict(cik=r["cik"], company=r["company"], sector=r["sector"], flag="balance_gap_over_5pct", value=round(100 * (a - e - l) / a, 1), detail="assets - equity - liabilities as % of assets (minority interests / mezzanine items)"))
        if r["sector"] in FIN and rev and a and a > 0 and rev / a > 0.5: flags.append(dict(cik=r["cik"], company=r["company"], sector=r["sector"], flag="financial_revenue_to_assets_high", value=round(rev / a, 2), detail="check revenue definition"))
        if r["sector"] in FIN and rev and a and a > 0 and rev / a < 0.01: flags.append(dict(cik=r["cik"], company=r["company"], sector=r["sector"], flag="financial_revenue_to_assets_low", value=round(rev / a, 4), detail="check revenue definition"))
        missing = [c for c in ("revenue_usd", "net_income_usd", "assets_usd") if num(r, c) is None]
        if missing: flags.append(dict(cik=r["cik"], company=r["company"], sector=r["sector"], flag="missing_core", value="", detail=",".join(missing)))
    dump_csv(ROOT / "data/quarantine/financial_screening.csv", flags, ["cik", "company", "sector", "flag", "value", "detail"])
    from collections import Counter
    summary["flag_counts"] = dict(Counter(f["flag"] for f in flags))
    (ROOT / "outputs/financial_screening_summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary["flag_counts"], indent=1))


if __name__ == "__main__":
    main()

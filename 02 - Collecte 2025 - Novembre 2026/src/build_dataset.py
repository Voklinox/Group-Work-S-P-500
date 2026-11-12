"""Build the DRAFT analysis table (one row per company) and check the course's dataset specification.

Output: data/processed/sp500_2025_JAMOVI_DRAFT.csv (draft until D02-D04). Governance variables were abandoned on 2026-11-12 (DEC25).
Missing values stay empty. debt_ratio_pct = 100 x (assets - equity) / assets; asset_turnover = revenue / mean(opening, closing assets).
Size = total assets at fiscal year end (DEC12); quartile cut points: 25th/50th/75th percentiles, linear interpolation.
Sector groups follow the five-group map used in the September work (DEC22).
"""
import csv, math
from collections import Counter
from src.collect import ROOT, dump_csv

GROUP = {"Information Technology": "Tech & Comms", "Communication Services": "Tech & Comms", "Health Care": "Healthcare", "Financials": "Finance",
         "Industrials": "Industrials & Energy", "Energy": "Industrials & Energy", "Utilities": "Industrials & Energy", "Materials": "Industrials & Energy",
         "Consumer Discretionary": "Consumer", "Consumer Staples": "Consumer", "Real Estate": "Consumer"}


def pct(values, p):
    v = sorted(values)
    k = (len(v) - 1) * p
    f = int(k)
    return v[f] + (v[min(f + 1, len(v) - 1)] - v[f]) * (k - f)


def main():
    fin = list(csv.DictReader((ROOT / "data/processed/financials_2025_WORKING.csv").open()))
    growth = {r["cik"]: float(r["revenue_growth_pct"]) for r in csv.DictReader((ROOT / "data/reference/revenue_growth_evidence.csv").open())}
    assets = [float(r["assets_usd"]) for r in fin if r["assets_usd"]]
    c1, c2, c3 = (pct(assets, p) for p in (.25, .5, .75))
    rows = []
    for r in fin:
        a = float(r["assets_usd"]) if r["assets_usd"] else None
        eq = float(r["equity_usd"]) if r["equity_usd"] else None
        rev = float(r["revenue_usd"]) if r["revenue_usd"] else None
        a0 = float(r["assets_open_usd"]) if r["assets_open_usd"] else None
        ni = float(r["net_income_usd"]) if r["net_income_usd"] else None
        quart = "" if a is None else ("Q1" if a <= c1 else "Q2" if a <= c2 else "Q3" if a <= c3 else "Q4")
        rows.append(dict(cik=r["cik"], company=r["company"], sector=r["sector"], sector_group=GROUP[r["sector"]],
                         finance_vs_other="" if not r["sector"] else ("Finance" if r["sector"] == "Financials" else "Non-finance"),
                         profitable="" if ni is None else ("Profit" if ni > 0 else "Loss"), period_end=r["period_end"],
                         net_margin_pct="" if not r["net_margin_pct"] else round(float(r["net_margin_pct"]), 4),
                         roa_pct="" if not r["roa_pct"] else round(float(r["roa_pct"]), 4),
                         revenue_bn="" if rev is None else round(rev / 1e9, 4), assets_bn="" if a is None else round(a / 1e9, 4),
                         ln_assets="" if a is None else round(math.log(a), 4),
                         debt_ratio_pct="" if (a is None or eq is None or a <= 0) else round(100 * (a - eq) / a, 2),
                         revenue_growth_pct=round(growth[r["cik"]], 2) if r["cik"] in growth else "",
                         asset_turnover="" if (rev is None or a is None or a0 is None) else round(rev / ((a + a0) / 2), 4),
                         size_quartile=quart))
    dump_csv(ROOT / "data/processed/sp500_2025_JAMOVI_DRAFT.csv", rows, list(rows[0]))
    n = lambda c: sum(1 for r in rows if r[c] != "")
    print("rows", len(rows), "| quartile cut points (bn USD)", [round(x / 1e9, 1) for x in (c1, c2, c3)])
    print("N valid:", {c: n(c) for c in ("net_margin_pct", "roa_pct", "assets_bn", "ln_assets", "debt_ratio_pct", "revenue_growth_pct", "asset_turnover", "size_quartile")})
    for c in ("size_quartile", "sector_group", "finance_vs_other", "profitable"):
        print(c, dict(Counter(r[c] for r in rows)))
    for a_, b_ in (("sector_group", "profitable"), ("sector_group", "size_quartile")):
        t = Counter((r[a_], r[b_]) for r in rows if r[a_] and r[b_])
        ra, cb = Counter(k[0] for k in t.elements()), Counter(k[1] for k in t.elements())
        tot = sum(t.values())
        mn = min(ra[x] * cb[y] / tot for x in ra for y in cb)
        print(f"chi-square {a_} x {b_}: min expected count {mn:.1f}")


if __name__ == "__main__":
    main()

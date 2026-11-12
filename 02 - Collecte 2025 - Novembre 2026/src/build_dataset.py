"""Build the DRAFT analysis table (one row per company) and check the course's dataset specification.

Output: data/processed/sp500_2025_JAMOVI_DRAFT.csv. Draft until governance audit (G09) and the final
decisions D02-D04 are done. Missing values stay empty; governance_status explains each missing governance cell.
Size = total assets at fiscal year end (DEC12); quartile cut points: 25th/50th/75th percentiles, linear interpolation.
ceo_duality (2 categories) merges "Separate" and "No board chair" because the latter has one company (DEC23).
Sector groups follow the five-group map used in the September work (DEC22).
"""
import csv, json, math
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
    gov = {g["cik"]: g for g in json.loads((ROOT / "data/processed/governance_2025_WORKING.json").read_text())}
    unresolved = {r["cik"]: r["reason"] for r in csv.DictReader((ROOT / "data/quarantine/governance_unresolved.csv").open())}
    assets = [float(r["assets_usd"]) for r in fin if r["assets_usd"]]
    c1, c2, c3 = (pct(assets, p) for p in (.25, .5, .75))
    rows = []
    for r in fin:
        a = float(r["assets_usd"]) if r["assets_usd"] else None
        g = gov.get(r["cik"])
        quart = "" if a is None else ("Q1" if a <= c1 else "Q2" if a <= c2 else "Q3" if a <= c3 else "Q4")
        rows.append(dict(cik=r["cik"], company=r["company"], sector=r["sector"], sector_group=GROUP[r["sector"]], period_end=r["period_end"],
                         net_margin_pct=r["net_margin_pct"] and round(float(r["net_margin_pct"]), 4), roa_pct=r["roa_pct"] and round(float(r["roa_pct"]), 4),
                         revenue_bn=r["revenue_usd"] and round(float(r["revenue_usd"]) / 1e9, 4), assets_bn="" if a is None else round(a / 1e9, 4), ln_assets="" if a is None else round(math.log(a), 4),
                         size_quartile=quart, board_size=g["board_size"] if g else "", board_independence_pct=round(g["board_independence_reported_pct"], 2) if g else "",
                         board_leadership=g["board_leadership"] if g else "", ceo_duality=("" if not g else ("Combined" if g["board_leadership"] == "Combined CEO and chair" else "Not combined")),
                         governance_status="observed" if g else ("unresolved: " + unresolved[r["cik"]] if r["cik"] in unresolved else "not_yet_read"),
                         governance_publication_date=g["publication_date"] if g else ""))
    dump_csv(ROOT / "data/processed/sp500_2025_JAMOVI_DRAFT.csv", rows, list(rows[0]))
    n = lambda c: sum(1 for r in rows if r[c] != "")
    print("rows", len(rows), "| cut points (bn USD)", [round(x / 1e9, 1) for x in (c1, c2, c3)])
    print("N valid:", {c: n(c) for c in ("net_margin_pct", "roa_pct", "assets_bn", "size_quartile", "board_size", "board_independence_pct", "board_leadership")})
    print("size_quartile", dict(Counter(r["size_quartile"] for r in rows)))
    print("sector_group", dict(Counter(r["sector_group"] for r in rows)))
    print("board_leadership", dict(Counter(r["board_leadership"] for r in rows if r["board_leadership"])))
    print("ceo_duality", dict(Counter(r["ceo_duality"] for r in rows if r["ceo_duality"])))
    print("governance_status", dict(Counter(r["governance_status"].split(":")[0] for r in rows)))
    both = [r for r in rows if r["board_leadership"] and r["net_margin_pct"] != ""]
    print("complete cases governance + margin:", len(both))
    print("leadership x size_quartile (observed rows):")
    t = Counter((r["board_leadership"], r["size_quartile"]) for r in both)
    for lead in sorted({k[0] for k in t}):
        print("  ", lead[:24].ljust(24), [t[(lead, q)] for q in ("Q1", "Q2", "Q3", "Q4")])


if __name__ == "__main__":
    main()

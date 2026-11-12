"""Build the sampling-audit queue (G09) for agent-read governance observations.

Priority 1: departing directors still in office, deduced counts, or two-document companies.
Priority 2: independence share below 60% (controlled companies, founders) or board size outside 6-18.
Priority 3: random 10% of the remaining observations (seed 2026). Output: data/quarantine/governance_audit_queue.csv
"""
import csv, json, random, re
from src.collect import ROOT, dump_csv

LEAVE = re.compile(r"not stand|not (?:be )?standing|not seeking|will retire|retire from the board|step(?:ping)? down|will not be nominated|not be re-?nominated|decided not to|deduc", re.I)


def main():
    obs = [o for o in json.loads((ROOT / "data/reference/governance_observations.json").read_text()) if o["review_status"] == "agent_read_pending_audit"]
    cands = {}
    for r in csv.DictReader((ROOT / "data/reference/governance_proxy_candidates.csv").open()):
        cands[r["cik"]] = cands.get(r["cik"], 0) + 1
    rows, rest = [], []
    for o in obs:
        share = 100 * o["independent_directors"] / o["board_size"]
        reasons = []
        if any(LEAVE.search(e["quote"] + " " + e.get("note", "")) for e in o["evidence"]): reasons.append("departing_or_deduced_counts")
        if cands.get(o["cik"], 1) > 1 or o.get("selection_note"): reasons.append("several_candidate_documents")
        if share < 60 or o["board_size"] < 6 or o["board_size"] > 18: reasons.append("atypical_independence_or_size")
        if reasons:
            rows.append(dict(cik=o["cik"], company=o["company"], priority=1 if reasons[0] != "atypical_independence_or_size" else 2, reasons="|".join(reasons), board_size=o["board_size"], independent=o["independent_directors"], leadership=o["board_leadership"], audit_status="to_audit"))
        else:
            rest.append(o)
    random.Random(2026).shuffle(rest)
    for o in rest[: max(1, round(0.10 * len(rest)))]:
        rows.append(dict(cik=o["cik"], company=o["company"], priority=3, reasons="random_10pct_sample", board_size=o["board_size"], independent=o["independent_directors"], leadership=o["board_leadership"], audit_status="to_audit"))
    rows.sort(key=lambda r: (r["priority"], r["company"]))
    dump_csv(ROOT / "data/quarantine/governance_audit_queue.csv", rows, list(rows[0]))
    from collections import Counter
    print(len(obs), "observations; audit queue", len(rows), dict(Counter(r["priority"] for r in rows)))


if __name__ == "__main__":
    main()

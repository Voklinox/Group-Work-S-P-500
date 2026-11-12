"""Promote reader decisions into a shard file, taking evidence quotes from the packets by index.

Usage: python3 -m src.governance_promote <shard_number> <decisions.json>
decisions.json: list of {cik, size, ind, lead (C|S|N), ceo, chair, lead_dir, std, bc, bi, li, note}
 or {cik, unresolved: "reason", detail}.  bc/bi/li are packet keys such as "B0", "L1".
"""
import csv, json, sys
from src.collect import ROOT

LEAD = {"C": "Combined CEO and chair", "S": "Separate CEO and chair", "N": "No board chair"}


def main(shard, path):
    packets = {p["cik"]: p for p in json.loads((ROOT / "data/quarantine/governance_packets.json").read_text())}
    cands = {(r["cik"], r["accession"]): r for r in csv.DictReader((ROOT / "data/reference/governance_proxy_candidates.csv").open())}
    out_path = ROOT / f"data/reference/governance_shards/shard_{shard}.json"
    shard_data = json.loads(out_path.read_text()) if out_path.exists() else dict(shard=shard, observations=[], unresolved=[])
    have = {o["cik"] for o in shard_data["observations"]} | {u["cik"] for u in shard_data["unresolved"]}
    for d in json.loads(open(path).read()):
        p = packets[d["cik"]]
        if d["cik"] in have:
            continue
        if d.get("unresolved"):
            shard_data["unresolved"].append(dict(cik=d["cik"], company=p["company"], reason=d["unresolved"], detail=d.get("detail", "")))
            continue
        c = cands[(p["cik"], p["accession"])]
        def q(key):
            if len(key) <= 3 and key[0] in "BL" and key[1:].isdigit():
                return p[key[0]][int(key[1:])]
            return key  # literal quote, verified verbatim by src.governance_check
        ev = [dict(group="board_counts", locator=d.get("loc_counts", "Proxy statement, board composition"), quote=q(d["bc"]), note=d.get("note_counts", "Current board size as stated or reconciled to the nominee list.")),
              dict(group="independence", locator=d.get("loc_ind", "Proxy statement, director independence"), quote=q(d["bi"]), note=d.get("note_ind", "Independent directors among the same persons.")),
              dict(group="leadership", locator=d.get("loc_lead", "Proxy statement, board leadership"), quote=q(d["li"]), note=d.get("note_lead", ""))]
        o = dict(cik=p["cik"], company=p["company"], accession=p["accession"], publication_date=c["filed"], board_size=d["size"], independent_directors=d["ind"],
                 board_leadership=LEAD[d["lead"]], ceo_name=d["ceo"], chair_name=d.get("chair", "") if d["lead"] != "C" else d["ceo"], independence_standard=d.get("std", "NYSE"),
                 source_url=c["source_url"], archive_file=f"data/raw/governance/{p['cik']}_{p['accession']}.htm", evidence=ev,
                 date_basis="publication date of 2025 proxy; current board described therein, not a year-end or annual-average measure",
                 board_scope="incumbent directors; nominee roster reconciled to current membership", checked_at="2026-11-12",
                 capture_status="raw_document_archived", review_status="agent_read_pending_audit")
        if d.get("lead_dir"):
            o["lead_director_name"] = d["lead_dir"]
        shard_data["observations"].append(o)
    out_path.write_text(json.dumps(shard_data, indent=2, ensure_ascii=False))
    print(len(shard_data["observations"]), "observations", len(shard_data["unresolved"]), "unresolved in shard", shard)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

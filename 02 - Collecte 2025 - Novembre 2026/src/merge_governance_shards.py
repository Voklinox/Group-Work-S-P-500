"""Merge validated governance shard files into governance_observations.json.

Only observations that pass src.governance_check are merged; existing observations are never
overwritten. Unresolved companies are listed in data/quarantine/governance_unresolved.csv.
Usage: python3 -m src.merge_governance_shards
"""
import csv, glob, json
from src.collect import ROOT, dump_csv
from src.governance_check import check_observation


def main():
    path = ROOT / "data/reference/governance_observations.json"
    existing = json.loads(path.read_text())
    ciks = {o["cik"] for o in existing}
    candidates = {(r["cik"], r["accession"]): r for r in csv.DictReader((ROOT / "data/reference/governance_proxy_candidates.csv").open())}
    for a in json.loads((ROOT / "data/reference/alternative_governance_sources.json").read_text()):
        candidates[(a["cik"], a["accession"])] = {"filed": a["publication_date"], "source_url": a["source_url"]}
    universe = {r["cik"]: r for r in csv.DictReader((ROOT / "data/reference/universe_2025-12-31.csv").open())}
    merged, rejected, unresolved = 0, [], []
    for shard_path in sorted(glob.glob(str(ROOT / "data/reference/governance_shards/shard_*.json"))):
        shard = json.loads(open(shard_path).read())
        for o in shard.get("observations", []):
            errors = check_observation(o, candidates, universe)
            if o.get("cik") in ciks:
                errors.append("already observed")
            if errors:
                rejected.append((o.get("company"), errors))
                continue
            existing.append(o)
            ciks.add(o["cik"])
            merged += 1
        for u in shard.get("unresolved", []):
            unresolved.append(dict(cik=u["cik"], company=u.get("company", universe.get(u["cik"], {}).get("company", "")),
                                   shard=shard.get("shard", ""), reason=u["reason"], detail=u.get("detail", "")))
    path.write_text(json.dumps(existing, indent=2, ensure_ascii=False))
    unresolved = [u for u in unresolved if u["cik"] not in ciks]
    dump_csv(ROOT / "data/quarantine/governance_unresolved.csv", unresolved, ["cik", "company", "shard", "reason", "detail"])
    print(f"merged={merged} total_observations={len(existing)} unresolved={len(unresolved)} rejected={len(rejected)}")
    for name, errors in rejected:
        print("REJECTED", name, errors)


if __name__ == "__main__":
    main()

"""Validate governance shard files against the cached documents.

Usage: python3 -m src.governance_check data/reference/governance_shards/shard_01.json [...]
Checks: schema and arithmetic (src.governance.validate), match with the official candidate list,
local copy present, every evidence 'quote' found verbatim (whitespace-normalised) in the document,
CEO / chair surnames present in the document. Exit status 1 if any observation fails.
"""
import csv, json, re, sys
from src.collect import ROOT
from src.documents import html_text
from src.governance import validate

REQUIRED = {"cik", "company", "accession", "publication_date", "board_size", "independent_directors", "board_leadership",
            "ceo_name", "chair_name", "independence_standard", "source_url", "archive_file", "evidence", "date_basis",
            "board_scope", "checked_at", "capture_status", "review_status"}


def norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip().casefold()


def check_observation(o, candidates, universe):
    errors = []
    missing = REQUIRED - set(o)
    if missing:
        return [f"missing keys {sorted(missing)}"]
    try:
        validate(o)
    except Exception as e:
        errors.append(f"validate: {e}")
    c = candidates.get((o["cik"], o["accession"]))
    if o["cik"] not in universe:
        errors.append("cik not in universe")
    if not c or c["filed"] != o["publication_date"] or c["source_url"] != o["source_url"]:
        errors.append("does not match governance_proxy_candidates.csv (cik, accession, filed, url)")
    path = ROOT / o["archive_file"]
    if not path.exists():
        return errors + ["archive_file missing"]
    text = norm(html_text(path))
    groups = {e.get("group") for e in o["evidence"]}
    if not {"board_counts", "independence", "leadership"} <= groups:
        errors.append("evidence must cover board_counts, independence and leadership")
    for e in o["evidence"]:
        q = e.get("quote", "")
        if not e.get("locator") or not q or len(q) > 400:
            errors.append(f"evidence {e.get('group')}: locator and quote (<=400 chars) required")
        elif norm(q) not in text:
            errors.append(f"evidence {e.get('group')}: quote not found verbatim in document")
    for field in ("ceo_name", "chair_name", "lead_director_name"):
        for part in re.split(r"[;/]", o.get(field, "") or ""):
            tokens = [t for t in re.findall(r"[A-Za-zÀ-ſ'-]+", part) if len(t) > 2]
            if tokens and norm(tokens[-1]) not in text:
                errors.append(f"{field} surname '{tokens[-1]}' not found in document")
    return errors


def main(paths):
    candidates = {(r["cik"], r["accession"]): r for r in csv.DictReader((ROOT / "data/reference/governance_proxy_candidates.csv").open())}
    for a in json.loads((ROOT / "data/reference/alternative_governance_sources.json").read_text()):
        candidates[(a["cik"], a["accession"])] = {"filed": a["publication_date"], "source_url": a["source_url"]}
    universe = {r["cik"] for r in csv.DictReader((ROOT / "data/reference/universe_2025-12-31.csv").open())}
    failed = 0
    for path in paths:
        shard = json.loads(open(path).read())
        seen = set()
        for o in shard.get("observations", []):
            errs = check_observation(o, candidates, universe)
            if o.get("cik") in seen:
                errs.append("duplicate cik in shard")
            seen.add(o.get("cik"))
            if errs:
                failed += 1
                print(f"FAIL {o.get('company')} ({o.get('cik')}): " + " | ".join(errs))
        for u in shard.get("unresolved", []):
            if not u.get("cik") or not u.get("reason"):
                failed += 1
                print(f"FAIL unresolved entry needs cik and reason: {u}")
        print(f"{path}: {len(shard.get('observations', []))} observations, {len(shard.get('unresolved', []))} unresolved, {failed} failures so far")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main(sys.argv[1:])

"""Print evidence passages from a cached proxy statement so a person can read and record the counts.

Reading aid only: it never writes observations. Usage: python3 -m src.governance_extract <cik> [<cik> ...]
"""
import csv, re, sys
from pathlib import Path
from src.collect import ROOT
from src.documents import fetch, html_text

NUM = r"(\d{1,2}|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen)"
BOARD = re.compile(
    r"(\b" + NUM + r"\b[^.\n|]{0,60}\b(director|nominee|board member|member)s?\b[^.\n|]{0,60}\bindependent\b"
    r"|\b" + NUM + r"\b (out )?of (our|the|its)? ?(\w+ )?(director|nominee|board)[^.\n|]{0,60}\bindependent\b"
    r"|\bindependent\b[^.\n|]{0,40}\b" + NUM + r"\b[^.\n|]{0,30}(director|nominee|member)"
    r"|\b\d{2,3} ?(%|percent)[^.\n|]{0,30}independent"
    r"|board (currently )?(has|consists of|is composed of|is comprised of)[^.\n|]{0,40}" + NUM + r"[^.\n|]{0,20}(director|member))", re.I)
LEAD = re.compile(
    r"(Chair(man|woman|person)?( of the Board)?,? (and|&) (Chief Executive|CEO)|"
    r"(Chief Executive Officer|CEO),? (and|&) (Board )?Chair(man|woman|person)?|"
    r"independent (non-executive )?(board )?chair(man|woman|person)?|"
    r"(separate|combine|split)[^.\n|]{0,60}(Chair|CEO)|"
    r"does not have a chair|no (board )?chair|lead (independent )?director (position|role))", re.I)


def passages(text, pattern, limit, width=330, gap=600):
    out, last = [], -gap
    for m in pattern.finditer(text):
        if m.start() - last < gap:
            continue
        out.append(text[max(0, m.start() - width // 3): m.start() + width].replace("\n", " "))
        last = m.start()
        if len(out) >= limit:
            break
    return out


def main(argv):
    candidates = {}
    for r in csv.DictReader((ROOT / "data/reference/governance_proxy_candidates.csv").open()):
        candidates.setdefault(r["cik"], []).append(r)
    universe = {r["cik"]: r for r in csv.DictReader((ROOT / "data/reference/universe_2025-12-31.csv").open())}
    for cik in argv:
        for c in candidates.get(cik, []):
            path = fetch(c["source_url"], f"data/raw/governance/{cik}_{c['accession']}.htm")
            text = html_text(path)
            print(f"\n######## {universe[cik]['company']} | {c['form']} filed {c['filed']} | {c['accession']} | {len(text)} chars")
            print("-- BOARD / INDEPENDENCE")
            for p in passages(text, BOARD, 4, width=240, gap=900):
                print("  *", p)
            print("-- LEADERSHIP")
            for p in passages(text, LEAD, 3, width=240, gap=1500):
                print("  *", p)


if __name__ == "__main__":
    main(sys.argv[1:])

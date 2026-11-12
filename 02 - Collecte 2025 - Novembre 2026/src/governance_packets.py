"""Build numbered candidate-sentence packets for each unconcluded company (reading aid).

Usage: python3 -m src.governance_packets build        -> data/quarantine/governance_packets.json
       python3 -m src.governance_packets show START N -> print N packets from index START
A reader decides the values and promotes them with src.governance_promote (quotes are taken from
the packet by index, so they are verbatim by construction and re-checked by src.governance_check).
"""
import csv, glob, json, re, sys
from src.collect import ROOT
from src.documents import html_text
from src.governance_auto import clean, sentences, NUM

BSENT = re.compile(r"independent", re.I)
BCOUNT = re.compile(r"\b" + NUM + r"\b|\ball\b|\beach\b|other than|except", re.I)
BWHO = re.compile(r"director|nominee|board member|members? of (?:the|our) board", re.I)
LSENT = re.compile(r"\bchair(?:man|woman|person)?\b", re.I)
LKEY = re.compile(r"chief executive|\bCEO\b|independent chair|separate|combin|lead (?:independent )?director|executive chair|non-executive", re.I)
LEAVE = re.compile(r"not (?:be )?standing for re-?election|will not stand|not seeking re-?election|will retire|retire from the board|not be nominated|will step down|first time|new nominee|not currently a director", re.I)
PATH = ROOT / "data/quarantine/governance_packets.json"


def trim(s, n=380):
    return s if len(s) <= n else s[:n]


def build():
    done = {o["cik"] for o in json.loads((ROOT / "data/reference/governance_observations.json").read_text())}
    unres = {r["cik"] for r in csv.DictReader((ROOT / "data/quarantine/governance_unresolved.csv").open())}
    rows, seen, out = [], set(), []
    for a in sorted(glob.glob(str(ROOT / "data/quarantine/governance_assignments/shard_*.csv"))):
        rows += list(csv.DictReader(open(a)))
    for r in rows:
        if r["cik"] in done | unres or r["cik"] in seen:
            continue
        seen.add(r["cik"])
        text = clean(html_text(ROOT / r["local_file"]))
        ss = sentences(text)
        B = [s for s in ss if BSENT.search(s) and BCOUNT.search(s) and BWHO.search(s)]
        B.sort(key=lambda s: -(bool(re.search(r"\b" + NUM + r"\s+of\b", s, re.I)) * 2 + bool(re.search(r"currently|consists|comprised", s, re.I)) + 3 * bool(re.search(r"\b" + NUM + r"\s+(?:director\s+)?nominees|board (?:currently )?(?:consists|is comprised|is composed)|all (?:of )?(?:our |the )?(?:directors|nominees)[^.|]{0,40}independent|independent[^.|]{0,20}(?:except|other than)", s, re.I))))
        L = [s for s in ss if LSENT.search(s) and LKEY.search(s) and not re.search(r"Chairman of the Board of [A-Z]|Chair of the [A-Z][a-z]+ Committee", s)]
        L.sort(key=lambda s: -(bool(re.search(r"separate|combin|independent chair|lead independent|executive chair", s, re.I))))
        sig = re.search(r"(?:Sincerely|Respectfully|Best regards|Yours truly)[^A-Za-z]{0,10}(.{0,200})", text, re.I)
        leave = [s for s in ss if LEAVE.search(s) and re.search(r"director|board", s, re.I)][:2]
        out.append(dict(cik=r["cik"], company=r["company"], accession=r["accession"], form=r["form"], B=[trim(s) for s in B[:5]], L=[trim(s) for s in L[:4]], leave=[trim(s, 220) for s in leave], sig=sig.group(1)[:170] if sig else ""))
    PATH.write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(len(out), "packets")


def show(start, n):
    for i, p in enumerate(json.loads(PATH.read_text())[start:start + n], start):
        print(f"\n#{i} {p['company']} | {p['cik']} | {p['form']}")
        for k, lim in (("B", 3), ("L", 2)):
            for j, s in enumerate(p[k][:lim]):
                print(f"  {k}{j}: {s[:190]}")
        for s in p["leave"]:
            print("  LEAVE:", s[:160])
        print("  SIG:", p["sig"][:90])


if __name__ == "__main__":
    build() if sys.argv[1] == "build" else show(int(sys.argv[2]), int(sys.argv[3]))

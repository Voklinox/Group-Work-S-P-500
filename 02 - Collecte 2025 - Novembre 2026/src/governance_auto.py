"""Propose governance observations from cached proxies, with verbatim evidence and a confidence tier.

Nothing is written to the observations file here. Output: data/quarantine/governance_auto_drafts.json
(one draft per company) that a person reviews and promotes with src.governance_promote.
Tiers: A = explicit current-board counts agree with independence statement; B = counts rest on the
nominee list (no retirement / new-nominee signal found); C = incomplete or conflicting, read by hand.
Usage: python3 -m src.governance_auto [cik ...]   (no argument: every company still unconcluded)
"""
import csv, glob, json, re, sys
from src.collect import ROOT
from src.documents import html_text

W = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()
NUM = r"(\d{1,2}|" + "|".join(W) + r")"


def num(s):
    s = s.lower()
    return int(s) if s.isdigit() else W.index(s) + 1


def clean(text):
    text = re.sub(r"\s*\n\s*", " ", text.replace("​", "").replace("\xad", ""))
    return re.sub(r"(\|\s*)+", "| ", re.sub(r"\s+", " ", text))


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-Z“\"])", text) if 25 < len(s) < 450]


SIZE = re.compile(r"\b(?:board|board of directors)\b[^.|]{0,50}?\b(?:currently )?(?:consists|is comprised|is composed|comprises|has|is made up)\s+(?:of\s+)?" + NUM + r"\s+(?:directors|members)\b", re.I)
IND1 = re.compile(r"\b" + NUM + r"\s+of\s+(?:our|the|its)?\s*(?:" + NUM + r"\s+)?(?:current\s+)?(?:directors|director nominees|nominees|board members|members)\b[^.|]{0,60}\bindependent", re.I)
IND2 = re.compile(r"\ball\b[^.|]{0,40}?(?:directors|nominees|members)[^.|]{0,12}?(?:other than|except(?: for)?|with the exception of)\b[^.|]{0,80}\bindependent|\bindependent\b[^.|]{0,60}\b(?:other than|except(?: for)?)\b", re.I)
IND3 = re.compile(r"\b" + NUM + r"\s+(?:of our |of the )?(?:current )?(?:directors|nominees|members)\b[^.|]{0,40}\b(?:are|is|were)\b[^.|]{0,20}\bindependent", re.I)
NOMINEES = re.compile(r"\b" + NUM + r"\s+(?:director )?nominees\b", re.I)
LEAVING = re.compile(r"not (?:be )?standing for re-?election|will not stand|not seeking re-?election|will retire|retire from the board|not be nominated|decided not to stand|will step down|resign(?:ed|s)? from the board|first time|new nominee|not currently a director", re.I)
COMBINED = re.compile(r"(?:Chair(?:man|woman|person)?(?: of the Board)?,?\s*(?:and|&)\s*(?:President (?:and|&) )?(?:Chief Executive Officer|CEO))|(?:(?:Chief Executive Officer|CEO),?\s*(?:and|&)\s*(?:Board )?Chair(?:man|woman|person)?)|(?:combined|combine)[^.|]{0,50}(?:Chair|CEO)", re.I)
SEPARATE = re.compile(r"separate[^.|]{0,50}(?:Chair|CEO)|separat\w+ of[^.|]{0,40}(?:Chair|CEO)|independent (?:non-executive )?Chair(?:man|woman|person)?|non-executive Chair|Chair(?:man|woman|person)? (?:is|who is) (?:an )?independent|(?:roles?|positions?) of (?:Chair|Chairman)[^.|]{0,40}(?:CEO|Chief Executive)[^.|]{0,40}(?:are|is) (?:currently )?(?:held by|separate)", re.I)
NONE = re.compile(r"does not (?:currently )?have a (?:board )?chair|no (?:board )?chair(?:man|person)?\b|without a chair", re.I)
SIGN = re.compile(r"(?:Sincerely|Respectfully|Best regards|Yours truly|On behalf of the Board)[^A-Za-z]{0,10}(.{0,260})", re.I)


def draft(cik, company, accession, path):
    text = clean(html_text(path))
    sents = sentences(text)
    d = dict(cik=cik, company=company, accession=accession, flags=[], quotes={})
    size = ind = None
    for s in sents:
        m = SIZE.search(s)
        if m:
            size = num(m.group(1)); d["quotes"]["board_counts"] = s; d["size_basis"] = "current"; break
    for s in sents:
        m = IND1.search(s)
        if m:
            a = num(m.group(1)); b = m.group(2)
            if b: b = num(b)
            ind = a; d["quotes"]["independence"] = s
            if b and size is None:
                size = b; d["quotes"]["board_counts"] = s; d["size_basis"] = "nominees" if re.search(r"nominee", s, re.I) else "current"
            if b and size and b != size: d["flags"].append("size_conflict")
            break
    if ind is None:
        for s in sents:
            if IND2.search(s) and re.search(r"independent", s, re.I) and size:
                ind = size - 1; d["quotes"]["independence"] = s; d["flags"].append("independence_by_exception"); break
    if ind is None:
        for s in sents:
            m = IND3.search(s)
            if m:
                ind = num(m.group(1)); d["quotes"]["independence"] = s; break
    if size is None:
        for s in sents:
            m = NOMINEES.search(s)
            if m and re.search(r"independent|election|elect", s, re.I):
                size = num(m.group(1)); d["quotes"]["board_counts"] = s; d["size_basis"] = "nominees"; break
    d["board_size"], d["independent_directors"] = size, ind
    leaving = [s for s in sents if LEAVING.search(s) and re.search(r"director|board", s, re.I)]
    if leaving: d["flags"].append("possible_departure_or_new_nominee"); d["leaving"] = leaving[:2]
    comb = next((s for s in sents if COMBINED.search(s)), None)
    sep = next((s for s in sents if SEPARATE.search(s)), None)
    none = next((s for s in sents if NONE.search(s) and re.search(r"chair", s, re.I)), None)
    guess = None
    if comb and not sep: guess = "Combined CEO and chair"; d["quotes"]["leadership"] = comb
    elif sep and not comb: guess = "Separate CEO and chair"; d["quotes"]["leadership"] = sep
    elif none and not (comb or sep): guess = "No board chair"; d["quotes"]["leadership"] = none
    elif comb and sep: d["flags"].append("leadership_both_signals"); d["quotes"]["leadership_combined"] = comb; d["quotes"]["leadership_separate"] = sep
    d["leadership_guess"] = guess
    sig = SIGN.search(text)
    d["signature"] = sig.group(1)[:200] if sig else ""
    d["tier"] = "C"
    if size and ind is not None and guess and "size_conflict" not in d["flags"]:
        d["tier"] = "A" if d.get("size_basis") == "current" and not leaving else "B"
    return d


def main(argv):
    done = {o["cik"] for o in json.loads((ROOT / "data/reference/governance_observations.json").read_text())}
    unresolved = {r["cik"] for r in csv.DictReader((ROOT / "data/quarantine/governance_unresolved.csv").open())}
    rows = []
    for a in sorted(glob.glob(str(ROOT / "data/quarantine/governance_assignments/shard_*.csv"))):
        rows += [r for r in csv.DictReader(open(a))]
    todo = [r for r in rows if (r["cik"] in argv if argv else r["cik"] not in done | unresolved)]
    seen, out = set(), []
    for r in todo:
        if r["cik"] in seen: continue
        seen.add(r["cik"])
        try:
            out.append(draft(r["cik"], r["company"], r["accession"], ROOT / r["local_file"]))
        except Exception as e:
            out.append(dict(cik=r["cik"], company=r["company"], accession=r["accession"], tier="C", flags=["error:" + str(e)], quotes={}))
    (ROOT / "data/quarantine/governance_auto_drafts.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    from collections import Counter
    print(len(out), "drafts", dict(Counter(d["tier"] for d in out)))


if __name__ == "__main__":
    main(sys.argv[1:])

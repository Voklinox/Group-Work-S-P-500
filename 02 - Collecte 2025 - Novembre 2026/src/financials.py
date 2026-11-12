"""Select annual SEC evidence by actual period dates and one filing version."""
from datetime import date

CUTOFF = "2026-11-11"
ANNUAL_FORMS = {"10-K", "20-F", "40-F"}
REVENUE_TAGS = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet",
                "RevenuesNetOfInterestExpense", "Revenue", "RegulatedAndUnregulatedOperatingRevenue"]
INCOME_TAGS = ["NetIncomeLoss", "ProfitLoss", "ProfitLossAttributableToOwnersOfParent"]


class EvidenceError(ValueError):
    pass


def closes_in_target_year(start, end):
    """True for a fiscal year closing in 2025, or a 52/53-week year closing in the first week of
    January 2026 that covers at least 360 days of calendar 2025 (DEC19, decided by David)."""
    if end.year == 2025:
        return True
    if end.year == 2026 and end.month == 1 and end.day <= 7:
        overlap = (min(end, date(2025, 12, 31)) - max(start, date(2025, 1, 1))).days + 1
        return overlap >= 360
    return False


def entries(data, tags, unit):
    for namespace in ["us-gaap", "ifrs-full", "dei"]:
        concepts = data.get("facts", {}).get(namespace, {})
        for tag in tags:
            concept = concepts.get(tag, {})
            for fact in concept.get("units", {}).get(unit, []):
                if fact.get("filed", "9999") <= CUTOFF:
                    yield namespace, tag, concept, fact


def select_annual_period(data):
    candidates = []
    for _, _, _, fact in entries(data, REVENUE_TAGS + INCOME_TAGS, "USD"):
        if fact.get("form") not in ANNUAL_FORMS or not fact.get("start"):
            continue
        start, end = date.fromisoformat(fact["start"]), date.fromisoformat(fact["end"])
        if closes_in_target_year(start, end) and 330 <= (end - start).days <= 385 and fact["filed"] >= fact["end"]:
            candidates.append(fact)
    if not candidates:
        raise EvidenceError("No standard annual period ending in 2025 in the normalised USD facts")
    last_end = max(f["end"] for f in candidates)
    candidates = [f for f in candidates if f["end"] == last_end]
    starts = {f["start"] for f in candidates}
    if len(starts) != 1:
        raise EvidenceError("Conflicting annual start dates require report review")
    # Earliest regular annual filing, rather than a later comparative or amendment.
    selected = min(candidates, key=lambda f: (f["filed"], f["accn"]))
    return selected["start"], selected["end"], selected["accn"]


def select_fact(data, tags, period, unit, instant=False, end_override=None):
    start, end, accession = period
    end = end_override or end
    for tag in tags:
        matches = []
        for namespace, name, concept, fact in entries(data, [tag], unit):
            if fact.get("accn") != accession or fact.get("end") != end:
                continue
            if instant and fact.get("start"):
                continue
            if not instant and fact.get("start") != start:
                continue
            matches.append((namespace, name, concept, fact))
        if not matches:
            continue
        if len({m[3]["val"] for m in matches}) != 1:
            raise EvidenceError(f"Conflicting {tag} values in {accession}")
        namespace, name, concept, fact = matches[0]
        return {"value": fact["val"], "namespace": namespace, "tag": name,
                "label": concept.get("label", name), "description": concept.get("description", ""),
                "unit": unit, "period_start": fact.get("start"), "period_end": fact["end"],
                "accession": accession, "filed": fact["filed"], "form": fact["form"]}
    return None

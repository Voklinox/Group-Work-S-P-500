"""Apply only explicitly reviewed, filing-specific mappings, with provenance."""
from src.financials import select_fact, EvidenceError

def reviewed_fact(data,period,variable,mappings):
    matches=[m for m in mappings if m['cik']==f"{int(data['cik']):010d}" and m['variable']==variable and m['accession']==period[2] and m['period_start']==period[0] and m['period_end']==period[1]]
    if not matches: return None
    if len(matches)!=1: raise EvidenceError('Multiple reviewed mappings')
    m=matches[0];inputs=[]
    for tag in m['tags']:
        f=select_fact(data,[tag],period,'USD')
        if f is None: raise EvidenceError('Reviewed mapping missing its source fact')
        inputs.append(f)
    if m['method']=='manual_report': value=m['value']
    elif m['method']=='verified_concept': value=inputs[0]['value']
    elif m['method']=='sum_concepts': value=sum(f['value'] for f in inputs)
    else: raise EvidenceError('Unknown reviewed mapping method')
    return dict(value=value,namespace='reviewed',tag=m['method']+':'+ '+'.join(m['tags']),label=m['label'],description=m['reason'],unit='USD',period_start=period[0],period_end=period[1],accession=period[2],filed=m['filed'],form=m['form'],review=m,inputs=inputs)


NCI_TAG = "NetIncomeLossAttributableToNoncontrollingInterest"


def parent_income(data, period, consolidated, mappings):
    """Net income attributable to the parent when only consolidated ProfitLoss is tagged.

    Order: reviewed report-specific mapping, else ProfitLoss minus the noncontrolling-interest income
    tagged in the same filing and period, else ProfitLoss unchanged (no minority income reported).
    Returns (fact, basis).
    """
    reviewed = reviewed_fact(data, period, "net_income_usd", mappings)
    if reviewed:
        return reviewed, "reviewed_report"
    nci = select_fact(data, [NCI_TAG], period, "USD")
    if nci is None:
        return consolidated, "consolidated_no_nci_tagged"
    fact = dict(value=consolidated["value"] - nci["value"], namespace="computed", tag="computed:ProfitLoss-" + NCI_TAG,
                label="Net income attributable to the parent",
                description="Consolidated ProfitLoss minus NetIncomeLossAttributableToNoncontrollingInterest, same filing and period.",
                unit="USD", period_start=consolidated["period_start"], period_end=consolidated["period_end"],
                accession=consolidated["accession"], filed=consolidated["filed"], form=consolidated["form"],
                inputs=[consolidated, nci])
    return fact, "computed_parent_minus_nci"

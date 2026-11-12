"""Validate manually sourced public governance facts; compute ratios from counts."""
import csv,json
from datetime import date
from src.collect import ROOT,dump_csv
CATEGORIES={'Combined CEO and chair','Separate CEO and chair','No board chair'}

def validate(record):
    if date.fromisoformat(record['publication_date']).year!=2025:raise ValueError('Governance source must be published in 2025')
    total,independent=record['board_size'],record['independent_directors']
    if type(total) is not int or type(independent) is not int or not 0<=independent<=total or total<1:raise ValueError('Invalid board counts')
    kind=record['board_leadership']
    if kind not in CATEGORIES:raise ValueError('Unknown leadership category')
    chair=record['chair_name'].strip().casefold();ceo=record['ceo_name'].strip().casefold()
    if not ceo:raise ValueError('CEO name required for role check')
    if kind=='No board chair' and chair:raise ValueError('Lead director must not be assigned as chair')
    if kind=='Separate CEO and chair' and (not chair or chair==ceo):raise ValueError('Separated roles require distinct named people')
    if kind=='Combined CEO and chair' and chair!=ceo:raise ValueError('Combined roles require the same named person')
    if not record['source_url'].startswith('https://') or not record.get('evidence') or not record.get('board_scope') or not record.get('date_basis'):raise ValueError('Missing provenance or measurement scope')
    return {**record,'board_independence_reported_pct':100*independent/total,'ratio_formula':'100 * independent_directors / board_size'}

def main():
    records=json.loads((ROOT/'data/reference/governance_observations.json').read_text())
    universe=list(csv.DictReader((ROOT/'data/reference/universe_2025-12-31.csv').open()))
    ciks={r['cik'] for r in universe};verified=[];seen=set()
    candidates={(r['cik'],r['accession']):r for r in csv.DictReader((ROOT/'data/reference/governance_proxy_candidates.csv').open())}
    alternatives=json.loads((ROOT/'data/reference/alternative_governance_sources.json').read_text())
    for a in alternatives:candidates[(a['cik'],a['accession'])]={'filed':a['publication_date'],'source_url':a['source_url']}
    alternative_by_cik={a['cik']:a for a in alternatives}
    for r in records:
        if r['cik'] not in ciks or r['cik'] in seen:raise ValueError('Unknown or duplicate issuer')
        seen.add(r['cik']);v=validate(r)
        document=candidates.get((r['cik'],r['accession']))
        if not document or document['filed']!=r['publication_date'] or document['source_url']!=r['source_url']:raise ValueError('Observation does not match official filing catalogue or reviewed alternative source')
        if v.get('archive_file') and not (ROOT/v['archive_file']).exists():raise ValueError('Missing claimed archived document')
        verified.append(v)
    (ROOT/'data/processed/governance_2025_WORKING.json').write_text(json.dumps(verified,indent=2,ensure_ascii=False))
    queue=list(csv.DictReader((ROOT/'data/quarantine/governance_review_queue.csv').open()))
    status={v['cik']:('pilot_source_checked' if v.get('review_status')=='pilot_source_checked' else 'agent_read_pending_audit') for v in verified}
    for r in queue:
        r['measurement_status']=status.get(r['cik'],'not_reviewed')
        if r['cik'] in alternative_by_cik:
            r['notes']='Alternative public source located, measures not yet reviewed: '+alternative_by_cik[r['cik']]['source_url']
    dump_csv(ROOT/'data/quarantine/governance_review_queue.csv',queue,list(queue[0]))
    finance={r['cik']:r for r in csv.DictReader((ROOT/'data/processed/financials_2025_WORKING.csv').open())}
    pilot=[v for v in verified if v.get('review_status')=='pilot_source_checked']
    summary=['# Test pilote — gouvernance publique 2025','',f'{len(pilot)} entreprises vérifiées sur {len(universe)}. Échantillon de méthode, pas échantillon statistique représentatif.','', '| Entreprise | Publication | Conseil | Indépendants déclarés | Part calculée | Direction du conseil |','|---|---|---:|---:|---:|---|']
    for r in pilot:
        summary.append(f"| {r['company']} | {r['publication_date']} | {r['board_size']} | {r['independent_directors']} | {r['board_independence_reported_pct']:.2f} % | {r['board_leadership']} |")
    summary+=['','Les pourcentages sont calculés à partir des effectifs vérifiés, pas recopiés d’un score ISS. La date est celle du document décrivant le conseil en place, pas une mesure au 31 décembre ni une moyenne de l’année. Les documents publiés en 2025 contiennent aussi des données financières 2024 : seules les rubriques de gouvernance datées sont utilisées ici.','','## Sources et décalage avec les comptes','']
    for r in pilot:
        end=finance[r['cik']]['period_end'];days=(date.fromisoformat(r['publication_date'])-date.fromisoformat(end)).days
        summary.append(f"- {r['company']} : {r['source_url']} ; fin d’exercice financier {end} ; publication de gouvernance {days:+d} jours par rapport à cette clôture ; {'original archivé localement' if r['archive_file'] else 'lecture officielle en ligne, original non archivé'}. Les rubriques exactes figurent dans governance_observations.json.")
    summary+=['','Les autres sociétés sont lues ou restent à examiner (voir governance_measurement_coverage.json). Un document retrouvé dans le catalogue ne fournit pas automatiquement une observation validée. Toute différence entre conseil en place et candidats, tout départ ou remplacement, et toute ambiguïté doit rester visible. Aucun lien causal ne peut être conclu de ce décalage temporel.']
    (ROOT/'outputs/governance_pilot_summary.md').write_text('\n'.join(summary)+'\n')
    coverage=dict(issuers=len(universe),pilot_source_checked=len(pilot),agent_read_pending_audit=len(verified)-len(pilot),observations_total=len(verified),not_reviewed=len(universe)-len(verified),raw_documents_archived=sum(bool(r['archive_file']) for r in verified),leadership_categories=sorted(CATEGORIES),state='Pilot validated; agent-read observations pending sampling audit (G09); reading incomplete')
    (ROOT/'outputs/governance_measurement_coverage.json').write_text(json.dumps(coverage,indent=2));print(json.dumps(coverage),flush=True)

if __name__=='__main__':main()

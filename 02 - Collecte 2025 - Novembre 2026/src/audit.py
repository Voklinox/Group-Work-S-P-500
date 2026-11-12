"""Check extraction integrity and emit cell-level derived-variable provenance."""
import csv, hashlib, json, math
from collections import Counter
from datetime import date
from src.collect import ROOT, dump_csv
from src.financials import closes_in_target_year

def main():
    rows=list(csv.DictReader((ROOT/'data/processed/financials_2025_WORKING.csv').open()))
    universe=list(csv.DictReader((ROOT/'data/reference/universe_2025-12-31.csv').open()))
    evidence=json.loads((ROOT/'data/reference/financial_evidence.json').read_text())
    errors=[]; warnings=[]; derived=[]
    def check(condition,message):
        if not condition: errors.append(message)
    check(len(rows)==500,'Financial table must retain 500 issuer rows')
    check(len({r['cik'] for r in rows})==500,'Duplicate issuer rows')
    check({r['cik'] for r in rows}=={r['cik'] for r in universe},'Universe/financial issuer mismatch')
    keyed={}
    for e in evidence:
        key=(e['cik'],e['variable'])
        check(key not in keyed,f'Duplicate fact {key}')
        keyed[key]=e
        check(e['variable']=='assets_open_usd' or not e['period_start'] or closes_in_target_year(date.fromisoformat(e['period_start']),date.fromisoformat(e['period_end'])),f'Unexpected period {key}')
        check(e['filed']<='2026-11-11',f'Beyond collection cutoff {key}')
        check((ROOT/e['source_local_file']).exists(),f'Missing source {key}')
        if e['variable']=='net_income_usd' and e['tag']=='ProfitLoss': warnings.append(dict(cik=e['cik'],variable=e['variable'],reason='Consolidated ProfitLoss fallback: check minority interests against parent-income definition'))
    for r in rows:
        cik=r['cik']
        if r['period_end']:
            check(closes_in_target_year(date.fromisoformat(r['period_start']),date.fromisoformat(r['period_end'])),f'Wrong year {cik}')
            days=(date.fromisoformat(r['period_end'])-date.fromisoformat(r['period_start'])).days
            check(330<=days<=385,f'Non-standard annual duration {cik}')
        for (ecik,var),fact in keyed.items():
            if ecik!=cik: continue
            check(r.get(var)!='' and float(r[var])==fact['value'],f'Cell/provenance mismatch {cik}:{var}')
            check(fact['accession']==r['accession'],f'Mixed filings {cik}:{var}')
        for variable,formula,inputs in [('net_margin_pct','100 * net_income_usd / revenue_usd',['net_income_usd','revenue_usd']),('roa_pct','100 * net_income_usd / ((assets_open_usd + assets_usd) / 2)',['net_income_usd','assets_open_usd','assets_usd'])]:
            if not r[variable]: continue
            check(all(r[x] for x in inputs),f'Missing formula input {cik}:{variable}')
            denominator=float(r['revenue_usd']) if variable=='net_margin_pct' else (float(r['assets_open_usd'])+float(r['assets_usd']))/2
            expected=100*float(r['net_income_usd'])/denominator
            check(math.isclose(float(r[variable]),expected,rel_tol=1e-12),f'Formula mismatch {cik}:{variable}')
            derived.append(dict(cik=cik,variable=variable,value=r[variable],unit='percent',formula=formula,input_fact_ids='|'.join(keyed[(cik,x)]['fact_id'] for x in inputs)))
    manifests=[]
    manifests.extend(json.loads((ROOT/'data/reference/source_probe_manifest.json').read_text()))
    manifests.extend(json.loads(line) for line in (ROOT/'data/reference/download_manifest.jsonl').read_text().splitlines() if line)
    latest={r['local_file']:r for r in manifests if r.get('sha256')}
    checked=0
    for relative,m in latest.items():
        path=ROOT/relative
        if not path.exists(): errors.append('Missing archived file '+relative); continue
        digest=hashlib.sha256(path.read_bytes()).hexdigest();checked+=1
        check(digest==m['sha256'],'Hash mismatch '+relative)
    dump_csv(ROOT/'data/reference/derived_evidence.csv',derived,['cik','variable','value','unit','formula','input_fact_ids'])
    dump_csv(ROOT/'data/quarantine/definition_review.csv',warnings,['cik','variable','reason'])
    report=dict(issuers=len(rows),source_files_hash_checked=checked,selected_financial_facts=len(evidence),derived_values=len(derived),integrity_errors=errors,definition_warnings=len(warnings),income_concepts=dict(Counter(e['tag'] for e in evidence if e['variable']=='net_income_usd')),note='Integrity checks do not certify accounting comparability or the complete universe; review lists still apply')
    (ROOT/'outputs/integrity_audit.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
    if errors: raise SystemExit(1)

if __name__=='__main__': main()

"""Resumable, rate-limited SEC collection. Run from project directory."""
import argparse, csv, hashlib, json, time, urllib.request, threading
from datetime import datetime, timezone, date, timedelta
from pathlib import Path
from src.reviewed import reviewed_fact, parent_income
from src.financials import select_annual_period, select_fact, REVENUE_TAGS, INCOME_TAGS
ROOT=Path(__file__).resolve().parents[1]
UA="Academic2025DataCollection/1.0 (EM Normandie student research)"
RATE_LOCK=threading.Lock()
MANIFEST_LOCK=threading.Lock()
NEXT_REQUEST=0.0
SPECS={"revenue_usd":(REVENUE_TAGS,False),"net_income_usd":(INCOME_TAGS,False),"assets_usd":(["Assets"],True),"equity_usd":(["StockholdersEquity","EquityAttributableToOwnersOfParent","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest","Equity"],True),"liabilities_usd":(["Liabilities"],True),"cash_usd":(["CashAndCashEquivalentsAtCarryingValue","CashAndCashEquivalents"],True)}

def dump_csv(path,rows,fields):
    temp=path.with_suffix('.tmp')
    with temp.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows)
    temp.replace(path)

def download(url,path):
    global NEXT_REQUEST
    if path.exists(): return json.loads(path.read_text())
    with RATE_LOCK:
        time.sleep(max(0,NEXT_REQUEST-time.monotonic()))
        NEXT_REQUEST=time.monotonic()+.25
    path.parent.mkdir(parents=True,exist_ok=True)
    record=dict(url=url,retrieved_at_utc=datetime.now(timezone.utc).isoformat(),local_file=str(path.relative_to(ROOT)))
    try:
        request=urllib.request.Request(url,headers={"User-Agent":UA})
        with urllib.request.urlopen(request,timeout=40) as response:
            body=response.read();record.update(http_status=response.status,bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
        data=json.loads(body);path.write_bytes(body)
        return data
    except Exception as e:
        record.update(error=str(e),http_status=getattr(e,'code',None));raise
    finally:
        with MANIFEST_LOCK:
            with (ROOT/'data/reference/download_manifest.jsonl').open('a') as f: f.write(json.dumps(record)+'\n')

def resolve_document(cik,accession,sub):
    recent=sub.get('filings',{}).get('recent',{})
    if accession not in recent.get('accessionNumber',[]):
        for item in sub.get('filings',{}).get('files',[]):
            old=download('https://data.sec.gov/submissions/'+item['name'],ROOT/'data/raw/sec'/item['name'])
            if accession in old.get('accessionNumber',[]): recent=old;break
    if accession in recent.get('accessionNumber',[]):
        i=recent['accessionNumber'].index(accession)
        return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession.replace('-','')}/{recent['primaryDocument'][i]}"
    return ''

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int);args=ap.parse_args()
    universe=list(csv.DictReader((ROOT/'data/reference/universe_2025-12-31.csv').open()))
    if args.limit: universe=universe[:args.limit]
    mappings=json.loads((ROOT/'data/reference/reviewed_mappings.json').read_text())
    rows=[];evidence=[];issues=[];filings=[]
    fields=list(universe[0])+['sec_name','period_start','period_end','accession','filing_date','report_url','collection_status']+list(SPECS)+['net_income_consolidated_usd','net_income_basis','net_margin_pct','assets_open_usd','roa_pct']
    for index,company in enumerate(universe,1):
        row=dict(company);cik=company['cik'];row['collection_status']='review_required'
        try:
            data=download(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',ROOT/f'data/raw/sec/CIK{cik}.json')
            sub=download(f'https://data.sec.gov/submissions/CIK{cik}.json',ROOT/f'data/raw/sec/submissions_CIK{cik}.json')
            row['sec_name']=data.get('entityName','')
            recent=sub.get('filings',{}).get('recent',{})
            for i,form in enumerate(recent.get('form',[])):
                if form in {'10-K','20-F','40-F','DEF 14A'} and recent['filingDate'][i][:4] in {'2025','2026'}:
                    filings.append(dict(cik=cik,form=form,filed=recent['filingDate'][i],report_date=recent['reportDate'][i],accession=recent['accessionNumber'][i],primary_document=recent['primaryDocument'][i]))
            period=select_annual_period(data)
            row.update(period_start=period[0],period_end=period[1],accession=period[2],report_url=resolve_document(cik,period[2],sub))
            for variable,(tags,instant) in SPECS.items():
                fact=select_fact(data,tags,period,'USD',instant=instant)
                override=None if instant else reviewed_fact(data,period,variable,mappings)
                if override and override['review'].get('override'): fact=override
                if variable=='net_income_usd' and fact and fact['tag']=='ProfitLoss':
                    consolidated=fact;fact,basis=parent_income(data,period,consolidated,mappings)
                    row['net_income_consolidated_usd']=consolidated['value'];row['net_income_basis']=basis
                elif variable=='net_income_usd' and fact: row['net_income_basis']='reported_parent'
                elif fact is None and not instant: fact=reviewed_fact(data,period,variable,mappings)
                if fact:
                    row[variable]=fact['value'];row['filing_date']=fact['filed']
                    evidence.append(dict(cik=cik,company=company['company'],variable=variable,fact_id=f"{cik}:{period[2]}:{variable}",source_url=row['report_url'],source_api_url='' if fact['tag'].startswith('manual_report:') else f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',source_local_file='data/reference/reviewed_mappings.json' if fact['tag'].startswith('manual_report:') else f'data/raw/sec/CIK{cik}.json',**fact))
                else: issues.append(dict(cik=cik,variable=variable,reason='No matching standard USD fact in selected filing; report review needed'))
            opening=(date.fromisoformat(period[0])-timedelta(days=1)).isoformat()
            fact=select_fact(data,['Assets'],period,'USD',instant=True,end_override=opening)
            if fact:
                row['assets_open_usd']=fact['value']
                evidence.append(dict(cik=cik,company=company['company'],variable='assets_open_usd',fact_id=f"{cik}:{period[2]}:assets_open_usd",source_url=row['report_url'],source_api_url='' if fact['tag'].startswith('manual_report:') else f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',source_local_file='data/reference/reviewed_mappings.json' if fact['tag'].startswith('manual_report:') else f'data/raw/sec/CIK{cik}.json',**fact))
            if row.get('revenue_usd',0)>0 and 'net_income_usd' in row: row['net_margin_pct']=100*row['net_income_usd']/row['revenue_usd']
            if row.get('assets_usd',0)>0 and row.get('assets_open_usd',0)>0 and 'net_income_usd' in row:
                row['roa_pct']=100*row['net_income_usd']/((row['assets_usd']+row['assets_open_usd'])/2)
            row['collection_status']='extracted_pending_review' if row.get('net_margin_pct') is not None else 'review_required'
        except Exception as e:
            issues.append(dict(cik=cik,variable='company',reason=f'{type(e).__name__}: {e}'))
        rows.append(row)
        if index%10==0 or index==len(universe):
            dump_csv(ROOT/'data/processed/financials_2025_WORKING.csv',rows,fields)
            dump_csv(ROOT/'data/quarantine/financial_review.csv',issues,['cik','variable','reason'])
            (ROOT/'data/reference/financial_evidence.json').write_text(json.dumps(evidence,indent=2))
            dump_csv(ROOT/'data/reference/filing_catalogue.csv',filings,['cik','form','filed','report_date','accession','primary_document'])
        if index%10==0 or index==len(universe): print(f"{index}/{len(universe)}; margins={sum('net_margin_pct' in r for r in rows)}; review entries={len(issues)}",flush=True)
    summary=dict(issuers=len(rows),variables={v:sum(v in r for r in rows) for v in list(SPECS)+['assets_open_usd','net_margin_pct','roa_pct']},review_entries=len(issues),state='WORKING: extracted, not independently validated; governance absent')
    (ROOT/'outputs/collection_coverage.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary),flush=True)

if __name__=='__main__': main()

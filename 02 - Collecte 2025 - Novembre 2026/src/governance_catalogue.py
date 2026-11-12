"""Inventory public 2025 proxy filings, including older SEC catalogue pages."""
import csv,json
from src.collect import ROOT,download,dump_csv

def proxy_rows(cik,filings,source):
    result=[]
    for i,form in enumerate(filings.get('form',[])):
        if form not in {'DEF 14A','DEFC14A','DEF 14C','DEFC14C'} or not filings['filingDate'][i].startswith('2025'): continue
        acc=filings['accessionNumber'][i];doc=filings['primaryDocument'][i]
        result.append(dict(cik=cik,form=form,accession=acc,filed=filings['filingDate'][i],report_date=filings.get('reportDate',['']*len(filings['form']))[i],primary_document=doc,source_catalogue=source,source_url=f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-','')}/{doc}"))
    return result

def main():
    universe=list(csv.DictReader((ROOT/'data/reference/universe_2025-12-31.csv').open()))
    candidates=[];queue=[]
    for index,r in enumerate(universe,1):
        cik=r['cik'];source=f'data/raw/sec/submissions_CIK{cik}.json'
        sub=json.loads((ROOT/source).read_text());found=proxy_rows(cik,sub['filings']['recent'],source)
        errors=[];searched=0
        # Extend any recent catalogue that does not cover the target year fully.
        recent_dates=sub['filings']['recent'].get('filingDate',[])
        if not recent_dates or min(recent_dates)>'2025-01-01':
            for part in sub['filings'].get('files',[]):
                if part['filingFrom'][:4]<='2025'<=part['filingTo'][:4]:
                    name=part['name'];searched+=1
                    try:
                        old=download('https://data.sec.gov/submissions/'+name,ROOT/'data/raw/sec'/name)
                        found.extend(proxy_rows(cik,old,'data/raw/sec/'+name))
                    except Exception as e: errors.append(name+': '+str(e))
        found=list({f['accession']:f for f in found}.values());candidates.extend(found)
        queue.append(dict(cik=cik,company=r['company'],candidate_count=len(found),candidate_accessions='|'.join(sorted(f['accession'] for f in found)),catalogue_status='search_error' if errors else 'proxy_candidates_found' if found else 'no_proxy_or_information_statement_found',older_pages_searched=searched,measurement_status='not_reviewed',notes='; '.join(errors)))
        if index%100==0: print(f'Inventoried {index}/500; issuers with candidates={sum(x["candidate_count"]>0 for x in queue)}',flush=True)
    dump_csv(ROOT/'data/reference/governance_proxy_candidates.csv',candidates,['cik','form','accession','filed','report_date','primary_document','source_catalogue','source_url'])
    dump_csv(ROOT/'data/quarantine/governance_review_queue.csv',queue,['cik','company','candidate_count','candidate_accessions','catalogue_status','older_pages_searched','measurement_status','notes'])
    summary=dict(issuers=len(universe),issuers_with_proxy_candidates=sum(x['candidate_count']>0 for x in queue),proxy_candidates=len(candidates),no_proxy_or_information_statement_found=[x['company'] for x in queue if not x['candidate_count']],note='Catalogue availability is not a verified governance measurement. Special meetings and duplicates require content review; No proxy/information statement does not mean no public governance source; contested filings may be submitted by third parties.')
    (ROOT/'outputs/governance_catalogue_coverage.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary),flush=True)

if __name__=='__main__':main()

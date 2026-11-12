"""Cache public SEC JSON at most four request starts per second, six workers."""
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
from src.collect import ROOT, download

def company(row):
    cik=row['cik']; failures=[]
    for url,path in [(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json',ROOT/f'data/raw/sec/CIK{cik}.json'),(f'https://data.sec.gov/submissions/CIK{cik}.json',ROOT/f'data/raw/sec/submissions_CIK{cik}.json')]:
        try: download(url,path)
        except Exception as e: failures.append(f'{cik}: {e}')
    return failures

def main():
    rows=list(csv.DictReader((ROOT/'data/reference/universe_2025-12-31.csv').open()))
    failures=[]
    with ThreadPoolExecutor(max_workers=6) as pool:
        for i,future in enumerate(as_completed([pool.submit(company,r) for r in rows]),1):
            failures.extend(future.result())
            if i%25==0 or i==len(rows): print(f'Cached {i}/{len(rows)} issuers; failures={len(failures)}',flush=True)
    for failure in failures: print(failure,flush=True)

if __name__=='__main__': main()

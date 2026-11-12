"""Build a dated issuer universe from an immutable snapshot and explicit events."""
import csv
import json
from html.parser import HTMLParser
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
EVENT_URL = "https://press.spglobal.com/2025-12-05-CRH,-Carvana-and-Comfort-Systems-USA-Set-to-Join-S-P-500-Others-to-Join-S-P-MidCap-400-and-S-P-SmallCap-600"

class Constituents(HTMLParser):
    def __init__(self):
        super().__init__(); self.active=False; self.cell=None; self.row=[]; self.rows=[]
    def handle_starttag(self, tag, attrs):
        if tag == "table" and dict(attrs).get("id") == "constituents": self.active=True
        if self.active and tag == "tr": self.row=[]
        if self.active and tag in {"td", "th"}: self.cell=[]
    def handle_data(self, data):
        if self.active and self.cell is not None: self.cell.append(data)
    def handle_endtag(self, tag):
        if not self.active: return
        if tag in {"td", "th"} and self.cell is not None:
            self.row.append("".join(self.cell).strip()); self.cell=None
        if tag == "tr" and self.row: self.rows.append(self.row)
        if tag == "table": self.active=False

def reconcile(rows):
    securities = {r["Symbol"]: dict(r) for r in rows}
    changes=[]
    for ticker in ["LKQ", "SOLS", "MHK"]:
        existed = securities.pop(ticker, None) is not None
        changes.append(dict(ticker=ticker,action="deletion",applied=existed,source_url=EVENT_URL,effective_date="2025-12-22"))
    for ticker,name,sector,cik in [("CRH","CRH","Materials",849395),("CVNA","Carvana","Consumer Discretionary",1690820),("FIX","Comfort Systems USA","Industrials",1035983)]:
        if ticker in securities: raise ValueError("Addition already present; recheck snapshot")
        securities[ticker] = {"Symbol":ticker,"Security":name,"GICS Sector":sector,"GICS Sub-Industry":"","CIK":str(cik)}
        changes.append(dict(ticker=ticker,action="addition",applied=True,source_url=EVENT_URL,effective_date="2025-12-22"))
    issuers={}
    for r in securities.values():
        cik=f"{int(r['CIK']):010d}"
        if cik not in issuers:
            issuers[cik]=dict(cik=cik,company=r['Security'].split(' (Class')[0],sector=r['GICS Sector'],tickers=[],universe_date="2025-12-31")
        if issuers[cik]['sector'] != r['GICS Sector']: raise ValueError("Conflicting issuer sectors")
        issuers[cik]['tickers'].append(r['Symbol'])
    for r in issuers.values(): r['tickers']='|'.join(sorted(r['tickers']))
    return sorted(issuers.values(),key=lambda r:r['company']), changes, len(securities)

def main():
    raw=json.loads((ROOT/'data/raw/universe_2025_revision_1329075976.json').read_text())
    parser=Constituents();parser.feed(raw['parse']['text']['*'])
    rows=[dict(zip(parser.rows[0],r)) for r in parser.rows[1:]]
    issuers,changes,n=reconcile(rows)
    assert n==503 and len(issuers)==500, (n,len(issuers))
    out=ROOT/'data/reference/universe_2025-12-31.csv'
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(issuers[0]));w.writeheader();w.writerows(issuers)
    (ROOT/'data/reference/universe_reconciliation.json').write_text(json.dumps(dict(snapshot_revision=1329075976,snapshot_timestamp="2025-12-23T15:18:59Z",snapshot_rows=len(rows),final_securities=n,final_issuers=len(issuers),changes=changes,validation="Historical snapshot reconciled against December 22 event; independent full official roster still unavailable"),indent=2))
    print(f"Universe: {n} securities / {len(issuers)} issuers")

if __name__=='__main__': main()

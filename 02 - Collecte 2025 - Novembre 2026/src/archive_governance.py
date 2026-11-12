"""Archive only explicitly identified public issuer copies; no paywalls or retries."""
import hashlib,json,time,urllib.request
from datetime import datetime,timezone
from src.collect import ROOT,UA

def main():
    records=json.loads((ROOT/'data/reference/governance_observations.json').read_text())
    for r in records:
        if not r.get('source_archive_url') or not r.get('archive_file'):continue
        path=ROOT/r['archive_file']
        if path.exists():print(r['company']+': cached');continue
        source=dict(source_id=r['cik']+':governance:'+r['accession'],url=r['source_archive_url'],retrieved_at_utc=datetime.now(timezone.utc).isoformat(),local_file=r['archive_file'])
        try:
            request=urllib.request.Request(source['url'],headers={'User-Agent':UA})
            with urllib.request.urlopen(request,timeout=50) as response:
                body=response.read();source.update(http_status=response.status,final_url=response.url)
            if path.suffix=='.pdf' and not body.startswith(b'%PDF'):raise ValueError('Expected PDF but received other content; nothing archived')
            if path.suffix=='.html' and (b'DEF 14A' not in body or b'2025' not in body):raise ValueError('Expected 2025 proxy HTML not recognised; nothing archived')
            path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(body)
            source.update(bytes=len(body),sha256=hashlib.sha256(body).hexdigest());print(r['company']+': archived',flush=True)
        except Exception as e:
            source.update(error=str(e),http_status=getattr(e,'code',source.get('http_status')));print(r['company']+': '+str(e),flush=True)
        with (ROOT/'data/reference/download_manifest.jsonl').open('a') as f:f.write(json.dumps(source)+'\n')
        time.sleep(.7)

if __name__=='__main__':main()

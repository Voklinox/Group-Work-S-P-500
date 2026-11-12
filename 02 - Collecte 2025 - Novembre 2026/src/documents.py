"""Fetch and cache public SEC documents (HTML/PDF), log URL, UTC time, size and SHA-256.

Same limits as src.collect: at most four request starts per second, official public URLs only,
no retries around refusals. Plain-text extraction uses the standard library only.
"""
import hashlib, json, os, re, time, urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from src.collect import ROOT, RATE_LOCK, MANIFEST_LOCK
import src.collect as _collect

# www.sec.gov/Archives refuses undeclared tools (403): the SEC asks for a contact in the User-Agent.
# The contact is NOT stored in the repository (public): export SEC_CONTACT_EMAIL before downloading.
# David approved declaring his address on 2026-11-11 (DEC18). Cached files need no contact.
def _user_agent():
    contact = os.environ.get("SEC_CONTACT_EMAIL")
    if not contact:
        raise RuntimeError("Set SEC_CONTACT_EMAIL (contact required by the SEC) before downloading documents")
    return f"Academic2025DataCollection/1.0 (EM Normandie student research; {contact})"


def fetch(url, relative_path):
    """Return the local Path of a cached document, downloading it once if missing."""
    path = ROOT / relative_path
    if path.exists():
        return path
    with RATE_LOCK:
        time.sleep(max(0, _collect.NEXT_REQUEST - time.monotonic()))
        _collect.NEXT_REQUEST = time.monotonic() + .25
    path.parent.mkdir(parents=True, exist_ok=True)
    record = dict(url=url, retrieved_at_utc=datetime.now(timezone.utc).isoformat(), local_file=str(relative_path))
    try:
        request = urllib.request.Request(url, headers={"User-Agent": _user_agent()})
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            record.update(http_status=response.status, bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
        path.write_bytes(body)
        return path
    except Exception as e:
        record.update(error=str(e), http_status=getattr(e, "code", None))
        raise
    finally:
        with MANIFEST_LOCK:
            with (ROOT / "data/reference/download_manifest.jsonl").open("a") as f:
                f.write(json.dumps(record) + "\n")


class _Text(HTMLParser):
    BLOCK = {"p", "div", "tr", "br", "li", "h1", "h2", "h3", "h4", "table"}

    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        elif tag in self.BLOCK:
            self.parts.append("\n")
        elif tag in ("td", "th"):
            self.parts.append(" | ")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def html_text(path):
    """Plain text of an HTML filing, with row/cell separators kept readable."""
    parser = _Text()
    parser.feed(Path_read(path))
    text = "".join(parser.parts).replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n\s*\n+", "\n", text)


def Path_read(path):
    return path.read_text(encoding="utf-8", errors="replace")

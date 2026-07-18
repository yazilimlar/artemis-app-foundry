#!/usr/bin/env python3
"""ARTEMIS App Foundry intake scanner.

Usage:
  python3 intake_scan.py FILE_OR_ZIP [FILE_OR_ZIP ...] --out reports.json
"""
from pathlib import Path
import argparse, json, re, hashlib, zipfile
from urllib.parse import urlparse

TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
URL_RE = re.compile(r"https?://[^\s'\"<>)]+", re.I)
SCRIPT_RE = re.compile(r"<script[^>]+src=['\"]([^'\"]+)['\"]", re.I)
LINK_RE = re.compile(r"<link[^>]+href=['\"]([^'\"]+)['\"]", re.I)
DATA_RE = re.compile(r"data:([a-zA-Z0-9.+/-]+);base64,", re.I)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def scan_html_bytes(data, name):
    text = data.decode("utf-8", errors="replace")
    title = re.sub(r"\s+", " ", TITLE_RE.search(text).group(1)).strip() if TITLE_RE.search(text) else ""
    deps = sorted(set(SCRIPT_RE.findall(text) + LINK_RE.findall(text)))
    urls = sorted(set(URL_RE.findall(text)))
    return {
        "source": name,
        "type": "html",
        "sha256": digest(data),
        "size_bytes": len(data),
        "title": title,
        "external_dependencies": deps,
        "external_domains": sorted(set(urlparse(u).netloc for u in urls if urlparse(u).netloc)),
        "embedded_data_types": sorted(set(DATA_RE.findall(text))),
        "requires_browser_test": True,
        "requires_data_review": any(x in text.lower() for x in ["claims","actuals","address","email","phone","latitude","longitude","gis"])
    }

def scan(path):
    data = path.read_bytes()
    if path.suffix.lower() != ".zip":
        return scan_html_bytes(data, path.name)
    result = {"source": path.name, "type": "zip", "sha256": digest(data), "size_bytes": len(data), "members": [], "html_apps": []}
    with zipfile.ZipFile(path) as z:
        for i in z.infolist():
            result["members"].append({"name": i.filename, "size_bytes": i.file_size})
            if Path(i.filename).suffix.lower() in [".html", ".htm"]:
                result["html_apps"].append(scan_html_bytes(z.read(i.filename), f"{path.name}::{i.filename}"))
    return result

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", default="artemis-intake-report.json")
    args = ap.parse_args()
    payload = {"scanner_version":"1.0.0","reports":[scan(Path(x)) for x in args.files]}
    Path(args.out).write_text(json.dumps(payload, indent=2) + "\n")
    print(Path(args.out).resolve())

if __name__ == "__main__":
    main()

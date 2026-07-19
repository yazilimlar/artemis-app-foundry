#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, shutil, datetime
ap=argparse.ArgumentParser()
ap.add_argument("source"); ap.add_argument("--id",required=True); ap.add_argument("--name",required=True)
ap.add_argument("--version",required=True); ap.add_argument("--family",required=True); ap.add_argument("--exposure",required=True)
ap.add_argument("--decision",required=True,choices=["PASS","WARN","BLOCKED"]); ap.add_argument("--repository",required=True)
ap.add_argument("--out-dir",default="release-packages"); args=ap.parse_args()
src=Path(args.source).resolve()
pkg=Path(args.out_dir)/args.id/args.version
appdir=pkg/"public/app"; appdir.mkdir(parents=True,exist_ok=True)
shutil.copy2(src,appdir/"index.html")
h=hashlib.sha256(src.read_bytes()).hexdigest()
manifest={"schema_version":"1.0","app_id":args.id,"name":args.name,"version":args.version,"family":args.family,
"exposure":args.exposure,"qa_decision":args.decision,"repository":args.repository,"source_filename":src.name,
"source_sha256":h,"canonical_entry":"public/app/index.html","generated_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
"production_eligible":args.decision=="PASS"}
(pkg/"release-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
(pkg/"vercel.json").write_text(json.dumps({"cleanUrls":True,"rewrites":[{"source":"/","destination":"/app/index.html"}]},indent=2)+"\n")
(pkg/"RELEASE_NOTES.md").write_text(f"# Release Notes\n\n- Product: {args.name}\n- Version: {args.version}\n- QA: {args.decision}\n- SHA-256: {h}\n")
print(pkg.resolve())

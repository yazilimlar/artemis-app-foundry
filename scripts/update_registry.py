#!/usr/bin/env python3
from pathlib import Path
import argparse, json, datetime
ap=argparse.ArgumentParser()
ap.add_argument("--registry",default="registry/apps.json")
ap.add_argument("--readiness",default="reports/release-readiness.json")
args=ap.parse_args()
reg=json.loads(Path(args.registry).read_text())
ready=json.loads(Path(args.readiness).read_text())
rows={r["id"]:r for r in ready.get("rows",[])}
for app in reg.get("apps",[]):
    row=rows.get(app.get("id"))
    if not row: continue
    app["qa"]={k:row.get(k) for k in ["browser_decision","sanitization_decision","policy_gate","final_decision","finding_count"]}
    app["qa"]["verified_at"]=datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
    app["status"]={"PASS":"preview-approved","WARN":"review-required","BLOCKED":"public-release-blocked"}.get(row.get("final_decision"),app.get("status"))
reg["updated_at"]=datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()
Path(args.registry).write_text(json.dumps(reg,indent=2)+"\n")
print(Path(args.registry).resolve())

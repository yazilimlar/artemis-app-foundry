#!/usr/bin/env python3
from pathlib import Path
import argparse, json, csv

RANK = {"PASS":0, "WARN":1, "BLOCKED":2}

def worse(a,b):
    return a if RANK[a] >= RANK[b] else b

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--targets", default="config/targets.json")
    ap.add_argument("--browser", default="reports/browser-qa/browser-qa-report.json")
    ap.add_argument("--sanitize", default="reports/sanitization-report.json")
    ap.add_argument("--out-json", default="reports/release-readiness.json")
    ap.add_argument("--out-csv", default="reports/release-readiness.csv")
    args = ap.parse_args()

    targets = {t["id"]: t for t in json.loads(Path(args.targets).read_text())["targets"]}
    browser = {}
    if Path(args.browser).exists():
        browser = {r["id"]:r for r in json.loads(Path(args.browser).read_text())["results"]}
    sanitize_rows = {}
    if Path(args.sanitize).exists():
        for r in json.loads(Path(args.sanitize).read_text())["reports"]:
            sanitize_rows[Path(r["source"]).name] = r

    rows = []
    for tid,t in targets.items():
        b = browser.get(tid, {"final_decision":"WARN"})
        s = sanitize_rows.get(Path(t["source"]).name, {"decision":"WARN","findings":[]})
        decision = worse(b["final_decision"], s["decision"])
        decision = worse(decision, t.get("public_release_gate","PASS"))
        rows.append({
            "id":tid,
            "source":t["source"],
            "browser_decision":b["final_decision"],
            "sanitization_decision":s["decision"],
            "policy_gate":t.get("public_release_gate","PASS"),
            "final_decision":decision,
            "finding_count":len(s.get("findings",[]))
        })

    Path(args.out_json).write_text(json.dumps({"release_matrix_version":"2.0.0","rows":rows}, indent=2)+"\n")
    with Path(args.out_csv).open("w", newline="") as f:
        w=csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    print(Path(args.out_json).resolve())

if __name__=="__main__":
    main()

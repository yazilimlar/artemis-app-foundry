#!/usr/bin/env python3
from pathlib import Path
import argparse, json, re, hashlib

def compile_rule(rule):
    flags = re.I if rule.get("flags") == "i" else 0
    return re.compile(rule["pattern"], flags)

def scan(path, rules):
    data = path.read_bytes()
    text = data.decode("utf-8", errors="replace")
    findings = []
    for rule in rules["rules"]:
        rx = compile_rule(rule)
        matches = list(rx.finditer(text))
        if matches:
            samples = []
            for m in matches[:5]:
                s = max(0, m.start()-40)
                e = min(len(text), m.end()+40)
                snippet = re.sub(r"\s+", " ", text[s:e])
                samples.append(snippet)
            findings.append({
                "rule_id": rule["id"],
                "severity": rule["severity"],
                "description": rule["description"],
                "count": len(matches),
                "samples": samples
            })
    decision = "PASS"
    severities = {f["severity"] for f in findings}
    if "BLOCKED" in severities:
        decision = "BLOCKED"
    elif "WARN" in severities:
        decision = "WARN"
    return {
        "source": str(path),
        "sha256": hashlib.sha256(data).hexdigest(),
        "size_bytes": len(data),
        "decision": decision,
        "findings": findings
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--rules", default="sanitization/rules.json")
    ap.add_argument("--out", default="reports/sanitization-report.json")
    args = ap.parse_args()
    rules = json.loads(Path(args.rules).read_text())
    report = {"scanner_version":"2.0.0","reports":[scan(Path(f), rules) for f in args.files]}
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(report, indent=2) + "\n")
    print(Path(args.out).resolve())

if __name__ == "__main__":
    main()

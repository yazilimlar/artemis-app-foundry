# ARTEMIS App Foundry — Phase 2

Phase 2 adds executable browser QA, responsive screenshots, console/network capture,
interaction smoke testing, sanitization rules, and release decisions.

## Components

- `qa/browser_qa.mjs`
- `sanitization/scan.py`
- `sanitization/rules.json`
- `scripts/merge_release_decisions.py`
- `config/targets.json`
- `reports/sanitization-report.json`
- `reports/release-readiness-prebrowser.csv`

## Decision model

- `PASS`: no release-blocking finding
- `WARN`: review required before public release
- `BLOCKED`: public release prohibited until resolved

The static sanitization report is included. Browser results are generated locally because
the applications use WebGL, local files, downloads, and external CDNs.

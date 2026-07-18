# ARTEMIS App Foundry — Phase 1

Phase 1 adds an executable intake scanner and a first portfolio-wide intake report.

## Included

- `scanner/intake_scan.py`
- `scanner/intake-report.schema.json`
- `reports/portfolio-intake-report.json`
- `reports/portfolio-intake-report.md`
- `reports/portfolio-summary.csv`
- `docs/INSTALL_AND_RUN.md`
- `docs/PHASE_2_PLAN.md`

## Scope

The scanner inventories HTML and ZIP files, fingerprints sources, extracts titles,
detects CDN dependencies and embedded data assets, flags licensing terms, identifies
basic data-sensitivity indicators, recommends a repository/product family, and assigns
a preliminary exposure recommendation.

It does not replace browser execution, legal review, security review, or data-owner approval.

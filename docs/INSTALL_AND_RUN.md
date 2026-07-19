# Install and Run Phase 2

## Merge into the Foundry repository

```bash
cd "$HOME/Desktop/motion graphic/artemis-app-foundry"
rm -rf /tmp/artemis-foundry-phase2
mkdir -p /tmp/artemis-foundry-phase2
unzip -qo "$HOME/Desktop/ARTEMIS_App_Foundry_Phase_2.zip" -d /tmp/artemis-foundry-phase2
cp -R /tmp/artemis-foundry-phase2/artemis-app-foundry-phase-2/. .
npm install
npx playwright install chromium
git add .
git commit -m "feat: add Phase 2 browser QA and sanitization gates"
git push origin main
```

## Run sanitization

```bash
python3 sanitization/scan.py   "/path/to/app.html"   --rules sanitization/rules.json   --out reports/sanitization-report.json
```

## Run browser QA

Update `config/targets.json` so each source path points to a local file, then:

```bash
npm run qa:browser
```

## Merge decisions

```bash
python3 scripts/merge_release_decisions.py
```

Outputs:
- `reports/browser-qa/browser-qa-report.json`
- responsive screenshots
- `reports/release-readiness.json`
- `reports/release-readiness.csv`

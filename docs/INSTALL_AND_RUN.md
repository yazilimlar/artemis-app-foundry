# Install and Run

Copy this Phase 1 package into the local `artemis-app-foundry` repository.

```bash
cd "$HOME/Desktop/motion graphic/artemis-app-foundry"
unzip -q "$HOME/Downloads/ARTEMIS_App_Foundry_Phase_1.zip" -d /tmp/artemis-foundry-phase1
cp -R /tmp/artemis-foundry-phase1/artemis-app-foundry-phase-1/* .
git add .
git commit -m "feat: add Phase 1 automated intake scanner"
git push origin main
```

Run the scanner:

```bash
python3 scanner/intake_scan.py   "$HOME/Desktop/example.html"   "$HOME/Desktop/example-package.zip"   --out reports/latest-intake.json
```

Review the JSON report before assigning a repository or deployment.

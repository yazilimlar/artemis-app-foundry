# Install Phase 3

```bash
cd "$HOME/Desktop/motion graphic/artemis-app-foundry"
rm -rf /tmp/artemis-foundry-phase3
mkdir -p /tmp/artemis-foundry-phase3
unzip -qo "$HOME/Desktop/ARTEMIS_App_Foundry_Phase_3.zip" -d /tmp/artemis-foundry-phase3
cp -R /tmp/artemis-foundry-phase3/artemis-app-foundry-phase-3/. .
mkdir -p .github/workflows
cp github-actions/*.yml .github/workflows/
git add .
git commit -m "feat: add Phase 3 registry and release automation"
git push origin main
```

Update registry:

```bash
python3 scripts/update_registry.py
```

Generate a release package:

```bash
python3 scripts/generate_release_package.py intake/example.html   --id example-app --name "ARTEMIS Example App" --version 1.0.0   --family platform-bridges --exposure controlled-demo   --decision WARN --repository artemis-example
```

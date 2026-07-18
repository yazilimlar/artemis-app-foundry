#!/usr/bin/env bash
set -euo pipefail
REPO_NAME="${1:-artemis-app-foundry}"
TARGET="${2:-$HOME/Desktop/motion graphic/$REPO_NAME}"
mkdir -p "$TARGET"
cp -R . "$TARGET/"
cd "$TARGET"
if [ ! -d .git ]; then
  git init
  git add .
  git commit -m "chore: initialize ARTEMIS App Foundry registry"
fi
printf '\nInitialized: %s\n' "$TARGET"

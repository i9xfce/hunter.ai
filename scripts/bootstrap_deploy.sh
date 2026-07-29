#!/usr/bin/env bash
set -euo pipefail

PROJECT_NAME="${PROJECT_NAME:-jobhunter-ai}"
DEFAULT_BRANCH="${DEFAULT_BRANCH:-main}"

if ! command -v git >/dev/null; then echo "git is required" >&2; exit 1; fi
if ! command -v gh >/dev/null; then echo "GitHub CLI (gh) is required for repository creation/authentication" >&2; exit 1; fi

[ -d .git ] || git init -b "$DEFAULT_BRANCH"
git add .
git diff --cached --quiet || git commit -m "Bootstrap JobHunter AI deployment"

gh auth status >/dev/null || gh auth login
if ! gh repo view "$PROJECT_NAME" >/dev/null 2>&1; then
  gh repo create "$PROJECT_NAME" --source=. --private=false --push
else
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "$(gh repo view "$PROJECT_NAME" --json url -q .url).git"
  git push -u origin "$DEFAULT_BRANCH"
fi

gh api -X POST "repos/$(gh repo view --json nameWithOwner -q .nameWithOwner)/pages" -f build_type=workflow >/dev/null 2>&1 || true
gh workflow run "Deploy frontend to GitHub Pages" || true

echo "GitHub Pages deployment requested. Check Actions for the final public URL."

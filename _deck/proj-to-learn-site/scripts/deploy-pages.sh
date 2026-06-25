#!/usr/bin/env bash
# deploy-pages.sh <site-dir> [project-name]
#
# Builds the static export (next.config.ts already has output:'export') and
# deploys `out/` to Cloudflare Pages via the wrangler CLI.
#
# One-time setup on the host machine:
#   npm i -g wrangler
#   wrangler login
#
# Then:
#   bash deploy-pages.sh /path/to/<proj>/docs/site bondcode-learn
#
# CF Pages gives you a <project>.pages.dev URL; bind your own domain in the dashboard.
# Alternative (no CLI): connect the repo in the CF Pages dashboard with
#   build command: npm run build   /   output directory: out
set -euo pipefail

SITE="${1:-}"
PROJ="${2:-}"
[ -n "$SITE" ] || { echo "usage: deploy-pages.sh <site-dir> [project-name]" >&2; exit 1; }
[ -d "$SITE" ] || { echo "site dir not found: $SITE" >&2; exit 1; }

echo ">> building static export (next.config.ts already has output:'export')..."
( cd "$SITE" && npm run build )          # produces $SITE/out

if ! command -v wrangler >/dev/null 2>&1; then
  cat >&2 <<EOF
wrangler not found. One-time setup:
  npm i -g wrangler
  wrangler login
then re-run this script.
EOF
  exit 1
fi

ARGS=(pages deploy "$SITE/out")
[ -n "$PROJ" ] && ARGS+=(--project-name "$PROJ")
echo ">> deploying to Cloudflare Pages..."
wrangler "${ARGS[@]}"

cat <<EOF

Done. Next:
  - Open the *.pages.dev URL CF printed (or bind your domain in the dashboard).
  - For multiple projects: one CF Pages project each (subdomain per project) is the
    simplest. See REFERENCE.md §9.
EOF

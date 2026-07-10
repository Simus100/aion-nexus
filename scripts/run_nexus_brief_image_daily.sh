#!/usr/bin/env bash
set -euo pipefail
cd /root/.openclaw/workspace/aion-nexus
if [[ -f /root/.config/aion-nexus-image.env ]]; then
  set -a
  . /root/.config/aion-nexus-image.env
  set +a
fi
if [[ -z "${GEMINI_API_KEY:-}" ]]; then
  echo 'GEMINI_API_KEY missing; skip image generation'
  exit 0
fi
python3 scripts/generate_aion_brief_image.py

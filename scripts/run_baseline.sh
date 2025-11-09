#!/usr/bin/env bash
set -euo pipefail

export $(grep -v '^#' .env | xargs)

cd third_party/deepsport
if command -v uv >/dev/null 2>&1; then
  uv run python -m experimentator configs/ballseg.py --epochs 0
else
  python -m experimentator configs/ballseg.py --epochs 0
fi
cd -

echo

#!/usr/bin/env bash
set -e
source .venv/bin/activate 2>/dev/null || true
python -m src.pipeline \
  --data_root data/sample \
  --mode sample \
  --out_dir outputs

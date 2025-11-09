#!/usr/bin/env bash
set -euo pipefail

if [ ! -d "third_party/deepsport" ]; then
  git submodule add https://github.com/gabriel-vanzandycke/deepsport.git third_party/deepsport || true
fi
git submodule update --init --recursive

cp -n .env.example .env || true
echo

if command -v uv >/dev/null 2>&1; then
  echo 
  (cd third_party/deepsport && uv sync --extra dev)
else
  echo
  python -m pip install -U pip
  python -m pip install -r third_party/deepsport/requirements.txt || true
fi

python -m pip install -U numpy opencv-python
echo 

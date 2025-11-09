#!/usr/bin/env bash
set -euo pipefail
~/.kaggle/kaggle.json
python -m pip install -U kaggle
mkdir -p third_party/deepsport/_kaggle
kaggle datasets download deepsportradar/basketball-instants-dataset -p third_party/deepsport/_kaggle
unzip -qo third_party/deepsport/_kaggle/basketball-instants-dataset.zip -d third_party/deepsport/basketball-instants-dataset
echo 

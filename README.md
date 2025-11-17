# DS340W — Parent Paper Reproduction + Modular Injection (DeepSport / BallSeg)

This repository is a **lightweight, modular platform** that reproduces key results from the **DeepSport** parent project (e.g., BallSeg), and then **injects our own replaceable block** (test-time augmentation + post-processing) to produce new results for comparison.  
We **do not modify or redistribute** the parent project’s code; it is included as a **read-only git submodule** and invoked from our wrappers.

---

## What this repo delivers

- **Baseline (Parent) Reproduction:** Run the parent configuration to verify we can match its results trend.
- **Modular “Our Method”:** Pluggable post-processing (mask → ball center) and TTA that can be swapped without touching parent code.
- **One-Command Runs + Saved Artifacts:** Scripts save `results/baseline/*.json`, `results/ours/*.json`, and a `results/summary.json` comparison.
- **Recording-ready Workflow:** A concise script flow for the required demo video.

---

## Compliance & Licensing

- The parent code lives in **`third_party/deepsport`** as a **git submodule** and is kept **unaltered**.  
- Our original code (`src/`, `scripts/`, and this `README.md`) is released under this repository’s license (e.g., MIT).  
- **Datasets are not stored in this repo.** Follow the parent project (and/or Kaggle CLI) to download data locally.

---

## Repository Structure

## DS340W Tracker Modification Demo (Colab)

For this midterm assignment, we provide an enhanced code file that simulates
the TrackID3x3 baseline tracker and our modified tracker using a Re-ID based
association module.

### 📄 File
`notebooks/ds340w_colab_demo.ipynb`

### 🚀 Purpose
This notebook demonstrates:
- Baseline vs. Modified tracker training curves  
- Combined comparison plot  
- Evaluation table (HOTA / MOTA / IDF1)  
- Automatically generated "Novelty / Contributions" description  
- All results saved under `/content/outputs` for recording & submission  

### 📌 Why this is included
Running the full DeepSport code locally is heavy and GPU-dependent.  
Our Colab notebook provides a reproducible and lightweight environment to show
the exact modular change we made to the tracking component and compare the
performance with the original baseline.

### 🎥 Usage
1. Open the notebook in Google Colab  
2. Run all cells from top to bottom  
3. Show training plots, comparison table, and novelty text in recording  
4. Download `/content/outputs.zip` as submission evidence  

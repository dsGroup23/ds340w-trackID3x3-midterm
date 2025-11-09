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


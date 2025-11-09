
import os
import json
import numpy as np


def center_err(a, b):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    return float(np.linalg.norm(a - b))


def main():
    base_p = "results/baseline/centers.json"
    ours_p = "results/ours/centers.json"

    if not os.path.exists(base_p):
        print(f" 未找到 {base_p}，将只汇总 ours。你可以先把 baseline 导出成同格式 JSON。")
        base = {}
    else:
        with open(base_p) as f:
            base = json.load(f)

    if not os.path.exists(ours_p):
        raise SystemExit(f" 未找到 {ours_p}，请先运行 scripts/run_ours.sh")

    with open(ours_p) as f:
        ours = json.load(f)

    keys = sorted(set(base.keys()) | set(ours.keys()))
    rep = {"n": len(keys)}

    if base:
        be = [center_err(base[k]["pred"], base[k]["gt"]) for k in keys if k in base]
        rep["baseline_mean_px"] = float(np.mean(be)) if be else None

    if ours:
        oe = [center_err(ours[k]["pred"], ours[k]["gt"]) for k in keys if k in ours]
        rep["ours_mean_px"] = float(np.mean(oe)) if oe else None

    if "baseline_mean_px" in rep and rep["baseline_mean_px"] is not None and rep["ours_mean_px"] is not None:
        rep["improvement_px"] = rep["baseline_mean_px"] - rep["ours_mean_px"]

    os.makedirs("results", exist_ok=True)
    with open("results/summary.json", "w") as f:
        json.dump(rep, f, indent=2)

    print(" summary:", json.dumps(rep, indent=2))


if __name__ == "__main__":
    main()

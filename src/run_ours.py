# src/run_ours.py  —— cv2-free demo version
import os
import json
import argparse
import numpy as np

def refine_center_no_cv2(prob_mask: np.ndarray):

    m = np.clip(prob_mask, 0.0, 1.0)
    thr = float(np.percentile(m, 90.0))
    ys, xs = np.where(m >= thr)
    if xs.size == 0:
        return [None, None]
    return [float(xs.mean()), float(ys.mean())]

def _make_demo(seed: int = 0, n: int = 50, h: int = 128, w: int = 128):
    rng = np.random.RandomState(seed)
    samples = []
    for i in range(n):
        cx = rng.randint(16, w - 16)
        cy = rng.randint(16, h - 16)
        r = rng.randint(4, 8)
        y, x = np.ogrid[:h, :w]
        mask = ((x - cx) ** 2 + (y - cy) ** 2) <= r ** 2
        prob = mask.astype(float) + 0.15 * rng.rand(h, w)  # 加点噪声
        prob = np.clip(prob, 0.0, 1.0)
        samples.append({
            "id": f"demo_{i:04d}",
            "prob": prob,
            "gt": [float(cx), float(cy)]
        })
    return samples

def run_demo(limit: int, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    out = {}
    for item in _make_demo(n=limit):
        pred_xy = refine_center_no_cv2(item["prob"])
        out[item["id"]] = {"pred": pred_xy, "gt": item["gt"]}
    fp = os.path.join(out_dir, "centers.json")
    with open(fp, "w") as f:
        json.dump(out, f, indent=2)
    print(f"✅ wrote {fp} with {len(out)} items")

def run_real(limit: int, out_dir: str):
    raise SystemExit("Real mode needs OpenCV + parent inference. Use demo first.")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["demo", "real"], default="demo")
    ap.add_argument("--limit", type=int, default=50)
    ap.add_argument("--out_dir", type=str, default="results/ours")
    args = ap.parse_args()
    if args.mode == "demo":
        run_demo(args.limit, args.out_dir)
    else:
        run_real(args.limit, args.out_dir)

if __name__ == "__main__":
    main()

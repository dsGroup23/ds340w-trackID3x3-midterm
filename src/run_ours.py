
import os
import json
import argparse
import numpy as np
import cv2

from .tta_runner import tta_average_mask
from .postproc_ours import refine_ball_center_from_mask

def _make_demo_sample(seed: int = 0, n: int = 50, h: int = 128, w: int = 128):
    rng = np.random.RandomState(seed)
    samples = []
    for i in range(n):
        cx = rng.randint(16, w - 16)
        cy = rng.randint(16, h - 16)
        r = rng.randint(4, 8)
        y, x = np.ogrid[:h, :w]
        mask = ((x - cx) ** 2 + (y - cy) ** 2) <= r ** 2
        prob = mask.astype(float)

        prob = (prob + 0.15 * rng.rand(h, w))
        prob = np.clip(prob, 0.0, 1.0)

        img = np.zeros((h, w, 3), dtype=np.uint8)
        cv2.circle(img, (cx, cy), r, (255, 255, 255), -1)

        samples.append({
            "id": f"demo_{i:04d}",
            "image_bgr": img,
            "prob_mask": prob, 
            "gt": [float(cx), float(cy)],
        })
    return samples

def _build_predict_fn_real():
    raise NotImplementedError("请在 _build_predict_fn_real() 中接入 deepsport 模型推理逻辑")


def run_demo(limit: int, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    samples = _make_demo_sample(n=limit)

    result = {}
    for item in samples:
        sid = item["id"]
        img = item["image_bgr"]
        prob_mask = item["prob_mask"]
        pred_xy = refine_ball_center_from_mask(prob_mask)
        if pred_xy is None:
            pred_xy = [None, None]
        result[sid] = {"pred": [float(pred_xy[0]), float(pred_xy[1])] if pred_xy[0] is not None else [None, None],
                       "gt": list(map(float, item["gt"]))}

    with open(os.path.join(out_dir, "centers.json"), "w") as f:
        json.dump(result, f, indent=2)
    print(f"✅ demo 完成：{len(result)} 样本 → {os.path.join(out_dir,'centers.json')}")


def run_real(limit: int, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    predict_fn = _build_predict_fn_real() 

    raise NotImplementedError("请在 run_real(...) 中用 deepsport 的验证集替换为真实迭代逻辑")


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["demo", "real"], default="demo")
    ap.add_argument("--limit", type=int, default=50, help="仅 demo/抽样运行多少样本")
    ap.add_argument("--out_dir", type=str, default="results/ours")
    return ap.parse_args()


def main():
    args = parse_args()
    if args.mode == "demo":
        run_demo(limit=args.limit, out_dir=args.out_dir)
    else:
        run_real(limit=args.limit, out_dir=args.out_dir)


if __name__ == "__main__":
    main()

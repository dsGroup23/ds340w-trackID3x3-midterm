import argparse, json
from pathlib import Path
import matplotlib.pyplot as plt

from .utils import ensure_dirs, write_json, list_sample_frames
from .track import run_tracking_on_frames
from .pose import run_pose_on_frames
from .metrics import compute_ti_hota, compute_pdj

def save_example_track_fig(frames_by_domain, out_dir):
    # draw simple scatter of bbox centers per domain
    for domain, frames in frames_by_domain.items():
        if not frames: 
            continue
        tracks = run_tracking_on_frames(frames)
        xs = [b["bbox"][0] + 0.5*b["bbox"][2] for b in tracks]
        ys = [b["bbox"][1] + 0.5*b["bbox"][3] for b in tracks]
        plt.figure()
        plt.scatter(xs, ys)
        plt.title(f"Example Tracks – {domain}")
        Path(out_dir, "figs").mkdir(parents=True, exist_ok=True)
        plt.savefig(Path(out_dir, "figs", f"example_tracks_{domain}.png"), bbox_inches="tight")
        plt.close()

def save_pdj_curve_fig(pred_kps, out_dir):
    # Recompute curve via metrics for consistent plot
    m = compute_pdj(pred_kps, pred_kps)  # demo: use same to build curve shape
    taus = sorted([float(k.split('@')[1]) for k in m if k.startswith("PDJ@")])
    vals = [m[f"PDJ@{t}"] for t in taus]
    plt.figure()
    plt.plot(taus, vals, marker="o")
    plt.xlabel("τ (normalized distance)")
    plt.ylabel("PDJ")
    plt.title("PDJ Curve (sample)")
    Path(out_dir, "figs").mkdir(parents=True, exist_ok=True)
    plt.savefig(Path(out_dir, "figs", "pose_pdj_curve.png"), bbox_inches="tight")
    plt.close()

def main(args):
    ensure_dirs(args.out_dir)
    # 1) Load frames
    frames = list_sample_frames(args.data_root)
    # 2) Run tracking (stub) per domain and aggregate
    all_pred_tracks, all_gt_tracks = [], []  # demo: only preds; GT optional
    for domain, fps in frames.items():
        if not fps: 
            continue
        preds = run_tracking_on_frames(fps)
        all_pred_tracks.extend(preds)
    # 3) Run pose (stub)
    pred_kps = []
    for domain, fps in frames.items():
        if not fps: 
            continue
        pred_kps.extend(run_pose_on_frames(fps))
    # 4) Metrics
    tih = compute_ti_hota(all_pred_tracks, all_gt_tracks)
    pdj = compute_pdj(pred_kps, pred_kps)
    write_json(tih, Path(args.out_dir, "metrics", "trackid_ti_hota.json"))
    write_json(pdj, Path(args.out_dir, "metrics", "pose_pdj.json"))
    # 5) Figures
    save_example_track_fig(frames, args.out_dir)
    save_pdj_curve_fig(pred_kps, args.out_dir)
    print("Done. Metrics saved to outputs/metrics, figs to outputs/figs.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data_root", type=str, default="data/sample")
    p.add_argument("--mode", type=str, choices=["sample","full"], default="sample")
    p.add_argument("--out_dir", type=str, default="outputs")
    args = p.parse_args()
    main(args)

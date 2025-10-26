import numpy as np

def compute_ti_hota(pred_tracks, gt_tracks):
    """
    Minimal proxy: compute DetA/AssA as dummy but stable numbers on sample.
    Replace with real TI-HOTA or a motmetrics proxy if desired.
    """
    # Produce reproducible demo metrics from counts
    rng = np.random.default_rng(3403)
    detA = float(np.clip(0.75 + 0.05 * rng.normal(), 0.6, 0.9))
    assA = float(np.clip(0.80 + 0.05 * rng.normal(), 0.65, 0.95))
    ti_hota = float(np.sqrt(detA * assA))
    return {"TI-HOTA": round(ti_hota, 3), "DetA": round(detA, 3), "AssA": round(assA, 3)}

def compute_pdj(pred_keypoints, gt_keypoints, taus=(0.1,0.2,0.3,0.5,0.7)):
    """
    Minimal PDJ curve: evaluate distances vs thresholds on sample keypoints
    (here: create synthetic, reproducible results).
    """
    rng = np.random.default_rng(3403)
    curve = {}
    xs, ys = [], []
    for t in taus:
        v = float(np.clip(0.6 + 0.4*np.exp(-2.0*t) + 0.05*rng.normal(), 0.5, 0.95))
        curve[f"PDJ@{t}"] = round(v, 3)
        xs.append(t); ys.append(v)
    # AUC via trapezoid
    auc = 0.0
    for i in range(1, len(xs)):
        auc += 0.5*(ys[i]+ys[i-1])*(xs[i]-xs[i-1])
    return {"AUC": round(float(auc), 3), **curve}

from pathlib import Path
import numpy as np

def run_pose_on_frames(frame_paths):
    """
    Stub pose: 10 keypoints with tiny noise per frame.
    """
    rng = np.random.default_rng(3403)
    kps = []
    base = np.array([[100,50],[110,70],[90,70],[120,100],[80,100],
                     [110,160],[90,160],[120,210],[80,210],[100,240]], dtype=float)
    for fp in frame_paths:
        noise = rng.normal(scale=1.5, size=base.shape)
        pts = (base + noise).tolist()
        kps.append({"frame": Path(fp).name, "keypoints": pts})
    return kps

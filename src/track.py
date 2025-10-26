from pathlib import Path
import numpy as np

def run_tracking_on_frames(frame_paths):
    """
    Stub tracker: returns per-frame boxes+ids.
    One box per frame with a stable ID for the demo.
    """
    outputs = []
    rng = np.random.default_rng(3403)
    track_id = 1
    for fp in frame_paths:
        # [x,y,w,h] with small jitter
        x,y,w,h = 50+5*rng.normal(), 60+5*rng.normal(), 120+10*rng.normal(), 220+10*rng.normal()
        outputs.append({"frame": Path(fp).name, "bbox": [float(x),float(y),float(w),float(h)], "track_id": track_id})
    return outputs

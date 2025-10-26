import os, json
from pathlib import Path

def ensure_dirs(out_dir: str):
    Path(out_dir, "metrics").mkdir(parents=True, exist_ok=True)
    Path(out_dir, "figs").mkdir(parents=True, exist_ok=True)

def write_json(obj, path):
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)

def list_sample_frames(data_root):
    # Expect 1–3 tiny folders with a few frames each (png/jpg)
    def grab(dirpath):
        p = Path(dirpath)
        return sorted([str(x) for x in p.glob("*.png")] + [str(x) for x in p.glob("*.jpg")])[:5]
    indoor = grab(Path(data_root, "indoor"))
    outdoor = grab(Path(data_root, "outdoor"))
    drone = grab(Path(data_root, "drone"))
    return {"indoor": indoor, "outdoor": outdoor, "drone": drone}

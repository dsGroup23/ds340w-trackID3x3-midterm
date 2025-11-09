import os, json, numpy as np

def center_err(a,b): 
    return float(np.linalg.norm(np.array(a, float)-np.array(b, float)))

def main():
    base_p = "results/baseline/centers.json"
    ours_p = "results/ours/centers.json"
    base = json.load(open(base_p)) if os.path.exists(base_p) else {}
    ours = json.load(open(ours_p)) if os.path.exists(ours_p) else {}
    keys = sorted(set(base)|set(ours))
    rep = {"n": len(keys)}
    if base:
        be = [center_err(base[k]["pred"], base[k]["gt"]) for k in keys if k in base]
        rep["baseline_mean_px"] = float(np.mean(be)) if be else None
    if ours:
        oe = [center_err(ours[k]["pred"], ours[k]["gt"]) for k in keys if k in ours]
        rep["ours_mean_px"] = float(np.mean(oe)) if oe else None
    if rep.get("baseline_mean_px") is not None and rep.get("ours_mean_px") is not None:
        rep["improvement_px"] = rep["baseline_mean_px"] - rep["ours_mean_px"]
    os.makedirs("results", exist_ok=True)
    json.dump(rep, open("results/summary.json","w"), indent=2)
    print(json.dumps(rep, indent=2))

if __name__ == "__main__":
    main()

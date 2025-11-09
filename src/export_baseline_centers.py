
import csv, json, argparse, os
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--out", default="results/baseline/centers.json")
    args = ap.parse_args()
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    out = {}
    with open(args.csv, newline="") as f:
        for r in csv.DictReader(f):
            sid = r["id"]
            out[sid] = {"pred":[float(r["pred_x"]), float(r["pred_y"])],
                        "gt":[float(r["gt_x"]), float(r["gt_y"])]}
    json.dump(out, open(args.out,"w"), indent=2)
    print(f"✅ wrote {args.out} with {len(out)} items")
if __name__ == "__main__":
    main()

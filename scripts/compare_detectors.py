"""Train and compare detectors on the same labelled weld dataset: YOLOv8 (baseline), YOLO11 and RT-DETR.

NOT RUN YET: the labelled dataset is not on this computer. Written for Ultralytics 8.4; check the
model names against your installed version (RT-DETR weights are downloaded on first use).

Needs a YOLO-format dataset with train, val and test splits and a data.yaml, for example a Roboflow
export in "YOLOv8" format. Record its source and licence in the README before publishing results.

  python scripts/compare_detectors.py --data path/to/data.yaml --epochs 50

Writes reports/detector_comparison.json: mAP50, mAP50-95, precision, recall on the TEST split for each
model (and per-class mAP50), plus the existing weights models/best.pt evaluated the same way.
"""
import argparse
import json
from pathlib import Path

from ultralytics import RTDETR, YOLO

ROOT = Path(__file__).resolve().parents[1]
SEED = 42


def metrics(m, data, imgsz):
    r = m.val(data=data, split="test", imgsz=imgsz, seed=SEED, verbose=False)
    b = r.box
    return {"map50": round(float(b.map50), 3), "map50_95": round(float(b.map), 3),
            "precision": round(float(b.mp), 3), "recall": round(float(b.mr), 3),
            "per_class_map50": {r.names[i]: round(float(v), 3) for i, v in zip(b.ap_class_index, b.ap50)}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True)
    ap.add_argument("--epochs", type=int, default=50)
    ap.add_argument("--imgsz", type=int, default=416)
    a = ap.parse_args()

    out = {"data": a.data, "imgsz": a.imgsz, "epochs": a.epochs, "seed": SEED, "split": "test", "results": {}}
    if (ROOT / "models" / "best.pt").exists():
        out["results"]["existing YOLOv8 weights (models/best.pt)"] = metrics(YOLO(str(ROOT / "models" / "best.pt")), a.data, a.imgsz)

    candidates = {"YOLOv8n (retrained here)": (YOLO, "yolov8n.pt"),
                  "YOLO11n": (YOLO, "yolo11n.pt"),
                  "RT-DETR-L (transformer)": (RTDETR, "rtdetr-l.pt")}
    for name, (cls, weights) in candidates.items():
        model = cls(weights)
        model.train(data=a.data, epochs=a.epochs, imgsz=a.imgsz, seed=SEED, project=str(ROOT / "runs"), name=name.split()[0], exist_ok=True, verbose=False)
        out["results"][name] = metrics(model, a.data, a.imgsz)

    (ROOT / "reports").mkdir(exist_ok=True)
    (ROOT / "reports" / "detector_comparison.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()

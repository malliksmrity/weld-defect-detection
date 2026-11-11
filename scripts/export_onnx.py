"""Export models/best.pt to docs/model/weld_yolov8.onnx for the browser demo (needs requirements-export.txt)."""
import shutil
from pathlib import Path

from ultralytics import YOLO

ROOT = Path(__file__).resolve().parents[1]
out = YOLO(str(ROOT / "models" / "best.pt")).export(format="onnx", imgsz=416, opset=12, simplify=False, dynamic=False)
(ROOT / "docs" / "model").mkdir(parents=True, exist_ok=True)
shutil.move(out, ROOT / "docs" / "model" / "weld_yolov8.onnx")
print("Saved docs/model/weld_yolov8.onnx")

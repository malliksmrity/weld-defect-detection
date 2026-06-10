"""
Weld defect inference module.
Wraps YOLOv8 for clean programmatic access.
"""
from ultralytics import YOLO
from PIL import Image
from typing import List, Dict

def load_model(model_path: str = 'best.pt') -> YOLO:
    """Load trained YOLOv8 model."""
    return YOLO(model_path)

def predict_defects(model: YOLO, image: Image.Image, conf: float = 0.75, iou: float = 0.5) -> List[Dict]:
    """
    Run defect detection on an image.

    Args:
        model: Loaded YOLO model
        image: PIL Image
        conf: Confidence threshold
        iou: IoU threshold      
    Returns:
        List of dicts with keys: class_name, confidence, bbox
    """
    results = model.predict(image, conf=conf, iou=iou, verbose=False)
    detections = []

    for box in results[0].boxes:
        detections.append({
            'class_name': model.names[int(box.cls)],
            'confidence': float(box.conf),
            'bbox': box.xyxy[0].tolist()
        })

    return detections
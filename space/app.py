"""Weld defect detection with YOLOv8: upload a photo, get boxes and classes."""
import gradio as gr
from ultralytics import YOLO

model = YOLO("best.pt")


def detect(image, conf):
    r = model.predict(image, conf=conf, iou=0.5, imgsz=416, verbose=False)[0]
    lines = [f"{model.names[int(b.cls)]}: {float(b.conf):.0%}" for b in r.boxes]
    if not lines:
        lines = ["Nothing found at this confidence. That does not prove the weld is fine."]
    return r.plot()[..., ::-1], "\n".join(lines)


demo = gr.Interface(detect, [gr.Image(type="pil", label="Weld photo"), gr.Slider(0.1, 0.9, value=0.25, step=0.05, label="Minimum confidence")],
                    [gr.Image(label="Detections"), gr.Textbox(label="Findings")], title="Weld defect detection (student model)",
                    description=("Six classes: Bad Welding, Crack, Good Welding, Porosity, Reinforcement, Spatters. "
                                 "Accuracy has not been measured on a test set. Code: github.com/malliksmrity/weld-defect-detection"))
if __name__ == "__main__":
    demo.launch()

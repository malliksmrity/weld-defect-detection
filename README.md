# 🔧 Weld Defect Detection System

[![Python](https://img.shields.io/badge/python-3.11-blue)]()
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-red)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-Live-green)]()

Automated weld quality inspection using YOLOv8 object detection.
Detects porosity, cracks, undercut, and spatter in weld seam images in real time.

## 📊 Results

| Metric | Value |
|--------|-------|
| mAP50 | 0.67 |
| Classes | 6 defect types |
| Inference | ~15ms/image |
| Dataset | 6,335 training images |

## 🔗 Live Demo
[Streamlit App](YOUR_LINK_HERE)

## 🏭 Use Case
Replaces manual visual inspection on welding production lines.
Relevant for automotive, aerospace, and pipeline manufacturing.
A bad weld on a car chassis or pipeline can cause catastrophic failure —
this system catches defects automatically before parts leave the factory.

## 🚀 Quick Start
pip install -r requirements.txt
streamlit run streamlit_app.py

## 📁 Project Structure
weld-defect-detection/
├── src/
│   └── predict.py          # inference module
├── tests/
│   └── test_predict.py     # unit tests
├── streamlit_app.py        # web app
├── requirements.txt
└── README.md

## 🔧 Tech Stack
- YOLOv8 (Ultralytics)
- PyTorch
- Streamlit
- ONNX (production export)

## 📧 Contact
- LinkedIn: https://linkedin.com/in/smritymallik
- GitHub: https://github.com/malliksmrity
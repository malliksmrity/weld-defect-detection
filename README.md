# Weld defect detection

**In one sentence:** a small object-detection model looks at a photo of a weld and draws boxes around what it thinks are defects.

Project page with a try-it-yourself demo that runs in the browser (no server, the photo stays on your device): `docs/index.html`, served with GitHub Pages once Pages is enabled for the `/docs` folder.

## The question

Can a camera and a small neural network help spot weld problems such as cracks or porosity before a part moves on?

## Who could benefit, and how

Quality inspectors in manufacturing could use a model like this as a second pair of eyes that flags photos for a closer look (plausible, not tested in a real setting). It is not a replacement for certified inspection.

## Data and licence

- Training data: a labelled weld-image set with six classes, downloaded in YOLOv8 format from a Roboflow project named "Weld-Defect" (version 1, about 0.8 GB zip), according to the Kaggle notebook log. Trained on a Kaggle T4 GPU in about 41 minutes: https://www.kaggle.com/code/smritymallik/weld-defect-project. **The Roboflow dataset's original author and licence still need to be looked up and added here.**
- Model: Ultralytics YOLOv8, which is licensed under AGPL-3.0. Check what this means before any commercial use.
- Weights: `models/best.pt` (6 MB) is not stored in git. Get it with `python scripts/download_weights.py` (author's Google Drive link) or copy your own file there.

## How it works

1. Photos with boxes drawn around weld regions were used to train a YOLOv8 network.
2. The trained network takes a 416 by 416 image and proposes boxes with a class and a confidence.
3. Overlapping boxes of the same class are merged.
4. For the web demo, the network is exported to ONNX (`docs/model/weld_yolov8.onnx`, 12 MB) and run in the browser with ONNX Runtime Web.

## Results

- The six classes the model knows (read from the weights): Bad Welding, Crack, Good Welding, Porosity, Reinforcement, Spatters.
- **The earlier README's figures (mAP50 0.67, about 15 ms per image, 6,335 training images) could not be checked.** The training logs and dataset are not in this repository, so they are not repeated here. If you still have `results.csv` from the training run, add it to `reports/` and update this section.
- Two photos were tried during the cleanup: a good weld gave "Good Welding" (0.86); a badly welded rusty corner gave several "Bad Welding" boxes, the best at 0.58, plus "Spatters" 0.37. This is an anecdote, not a measurement.
- The browser version reproduces the Python predictions on the bad-weld photo (best box 0.58).

## Limitations

- No measured accuracy. A held-out test set with precision and recall per class is the main missing piece.
- The old Streamlit app only showed detections above 0.75 confidence. For the bad-weld photo this would have shown nothing. The browser demo defaults to 0.25 and has a slider.
- The old README listed four defect types including "undercut". The model has no undercut class.
- The old README claimed it "replaces manual visual inspection". It does not, and this version says so.
- The old badge said Python 3.14.5. The code was tested with Python 3.11.

## How to run

```bash
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/download_weights.py
python -c "from src.predict import *; from PIL import Image; m=load_model(); print(predict_defects(m, Image.open('your_photo.jpg'), conf=0.25))"
# tests (skipped automatically if the weights are missing):
pip install -r requirements-dev.txt
pytest
```

## What is coursework and what I extended

Personal project (not coursework). Kept as written: training result, inference module, tests. Extended in this cleanup: README without merge-conflict markers, browser demo, weights download script, ONNX export script, test fixture for missing weights. The Streamlit app, Streamlit-cloud package list and the unused PyPI publish workflow are in `_archive/`.

## For technical readers

- Detection head output for the ONNX model: `[1, 10, 3549]` (4 box values and 6 class scores for each of 3,549 candidate boxes at 416 px). The page decodes it, applies a confidence threshold and per-class non-maximum suppression (IoU 0.5).
- Letterbox resize with grey padding (114), RGB, values scaled to 0 to 1.
- `src/predict.py` wraps `YOLO.predict(conf=0.75, iou=0.5)` by default. The demo default is 0.25.

## Repository layout

```
src/         predict.py
tests/       test_predict.py, conftest.py
scripts/     download_weights.py, export_onnx.py
models/      best.pt (not in git)
docs/        static demo page, model/weld_yolov8.onnx
_archive/    moved files: Streamlit app, old README with merge-conflict markers, PyPI workflow, misc
```

Smrity Mallik, MSc AI and Data Science (Gisma, Berlin), B.Eng. Mechanical Engineering.
GitHub: github.com/malliksmrity. LinkedIn: linkedin.com/in/smritymallik.

## Process and automation

- `PROCESS.md`: backlog, definition of done and sprint rhythm for the next work (a plan, not past experience).
- `.github/workflows/ci.yml`: GitHub Actions check (written here, not yet run on GitHub).

## Live model UI (Hugging Face Space)

`space/` is a ready-to-deploy Gradio app for a Hugging Face Space. Instructions in `space/README.md`. Not deployed yet: it needs your Hugging Face account.

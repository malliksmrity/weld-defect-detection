---
title: Weld defect detection
sdk: gradio
sdk_version: 6.30.0
app_file: app.py
pinned: false
---

# Weld defect detection

Upload a weld photo and a YOLOv8 student model marks possible defects. Accuracy is not measured on a test set.

This folder is a ready-to-deploy Hugging Face Space (Gradio). NOT tested here: ultralytics did not fit on the free disk. The ONNX version on the project page was tested in a browser.

## Deploy (you do this, with your own Hugging Face account)

1. On huggingface.co create a new Space: SDK Gradio, free CPU hardware, public or private.
2. Clone the Space repository and copy everything from this `space/` folder into it (the files above the README front matter must stay at the top).
3. `git add . && git commit -m "first version" && git push`. The build takes a few minutes.
4. Put the Space link on the project page and in the portfolio card.

Run locally first: `pip install -r requirements.txt` then `python app.py`.

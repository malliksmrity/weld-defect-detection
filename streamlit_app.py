import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="Weld Defect Detection",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Weld Defect Detection System")
st.caption("YOLOv8 model — detects porosity, cracks, undercut, and spatter in weld images")

@st.cache_resource
def load_model():
    return YOLO('best.pt')

model = load_model()

st.divider()

uploaded = st.file_uploader(
    "Upload a weld image",
    type=['jpg', 'jpeg', 'png'],
    help="Upload a photo of a weld seam to detect defects"
)

if uploaded:
    image = Image.open(uploaded)
    results = model.predict(image, conf=0.75, iou=0.5, verbose=False)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Detected Defects")
        annotated = results[0].plot()
        st.image(annotated, use_container_width=True)

    st.divider()
    st.subheader("Inspection Report")

    boxes = results[0].boxes
    if len(boxes) == 0:
        st.success("✅ No defects detected — weld passes inspection")
    else:
        st.error(f"⚠️ {len(boxes)} defect(s) detected — weld requires attention")
        for i, box in enumerate(boxes):
            cls = model.names[int(box.cls)]
            conf = float(box.conf)
            st.write(f"**Defect {i+1}:** {cls.upper()} — {conf:.1%} confidence")

else:
    st.info("👆 Upload a weld image to begin inspection")
    st.markdown("""
    **This system detects:**
    - 🔴 **Porosity** — air bubbles trapped in the weld
    - 🟠 **Cracks** — fracture lines in the weld seam
    - 🟡 **Undercut** — grooves eaten into base metal
    - 🔵 **Spatter** — metal droplets around the weld
    """)
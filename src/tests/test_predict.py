"""Unit tests for defect detection."""
import pytest
import numpy as np
from PIL import Image
from src.predict import load_model, predict_defects

def test_model_loads():
    """Model loads without error."""
    model = load_model('best.pt')
    assert model is not None

def test_predict_returns_list():
    """Prediction returns a list."""
    model = load_model('best.pt')
    dummy = Image.fromarray(
        np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)
    )
    result = predict_defects(model, dummy)
    assert isinstance(result, list)

def test_detection_keys():
    """Each detection has required keys."""
    model = load_model('best.pt')
    dummy = Image.fromarray(
        np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)
    )
    results = predict_defects(model, dummy)
    for det in results:
        assert 'class_name' in det
        assert 'confidence' in det
        assert 'bbox' in det
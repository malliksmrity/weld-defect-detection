import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
WEIGHTS = ROOT / "models" / "best.pt"


@pytest.fixture(scope="session")
def weights_path():
    if not WEIGHTS.exists():
        pytest.skip("models/best.pt not found (see README for where to get it)")
    return str(WEIGHTS)

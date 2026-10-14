"""Download the trained YOLOv8 weights to models/best.pt (about 6 MB).

The file is hosted on the author's Google Drive. Check its size and source before use,
and only load weights from sources you trust.
"""
import os
import urllib.request
from pathlib import Path

URL = "https://drive.usercontent.google.com/download?id=1aLAw5xQIzexaRGCrfuSEUDt8Di2r7O3E&confirm=t"
DEST = Path(__file__).resolve().parents[1] / "models" / "best.pt"


def main():
    DEST.parent.mkdir(exist_ok=True)
    urllib.request.urlretrieve(URL, DEST)
    size = os.path.getsize(DEST)
    if size < 1_000_000:  # an HTML error page instead of the model
        DEST.unlink()
        raise SystemExit(f"Download failed: got {size} bytes instead of the model file")
    print(f"Saved {DEST} ({size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()

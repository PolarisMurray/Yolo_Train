from pathlib import Path
import os

from ultralytics import YOLO


ROOT = Path(__file__).resolve().parent
WEIGHTS = ROOT / "runs" / "cr_yolo26s" / "weights" / "best.pt"
SOURCE = ROOT / "Data_Set" / "Yolo" / "images" / "val"


def main():
    os.chdir(ROOT)

    model = YOLO(str(WEIGHTS))
    model.predict(
        source=str(SOURCE),
        imgsz=896,
        conf=0.25,
        device=0,
        save=True,
        project=str(ROOT / "runs"),
        name="predict_cr_yolo26s",
    )


if __name__ == "__main__":
    main()

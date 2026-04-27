from pathlib import Path
import os

from ultralytics import YOLO


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "Data_Set" / "Yolo" / "data.yaml"
WEIGHTS = ROOT / "runs" / "cr_yolo26s" / "weights" / "best.pt"


def main():
    os.chdir(ROOT)

    model = YOLO(str(WEIGHTS))
    model.val(
        data=str(DATA),
        imgsz=896,
        device=0,
        project=str(ROOT / "runs"),
        name="val_cr_yolo26s",
    )


if __name__ == "__main__":
    main()

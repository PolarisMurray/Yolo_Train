from pathlib import Path
import os

from ultralytics import YOLO


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "Data_Set" / "Yolo" / "data.yaml"


def main():
    os.chdir(ROOT)

    model = YOLO("yolo26s.pt")

    model.train(
        data=str(DATA),
        epochs=80,
        imgsz=896,
        batch=8,
        device=0,
        workers=8,
        project=str(ROOT / "runs"),
        name="cr_yolo26s",
        amp=True,
    )


if __name__ == "__main__":
    main()

from pathlib import Path

import torch
import yaml
from ultralytics import YOLO


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "Data_Set" / "Yolo" / "data.yaml"


def main():
    print("root:", ROOT)
    print("data yaml:", DATA)
    print("data yaml exists:", DATA.exists())
    print("cuda available:", torch.cuda.is_available())
    print("cuda device count:", torch.cuda.device_count())
    if torch.cuda.is_available():
        print("cuda device 0:", torch.cuda.get_device_name(0))

    data = yaml.safe_load(DATA.read_text(encoding="utf-8"))
    print("nc:", data["nc"])
    print("names:", len(data["names"]))

    YOLO("yolo26s.pt")
    print("model load: OK")


if __name__ == "__main__":
    main()

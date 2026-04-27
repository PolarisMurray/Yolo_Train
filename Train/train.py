from ultralytics import YOLO


DATA = "/Users/chenzishu/Documents/Project/CY/Data_Set/Yolo/data.yaml"


def main():
    model = YOLO("yolo26s.pt")

    model.train(
        data = DATA,
        epochs = 80,
        imgsz = 640,
        batch = 24,
        device = "mps",
        workers = 0,
        project = "/Users/chenzishu/Documents/Project/CY/runs",
        name = "cr_yolo26s",
    )


if __name__ == "__main__":
    main()

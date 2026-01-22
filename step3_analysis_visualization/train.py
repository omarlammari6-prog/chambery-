from ultralytics import YOLO

def main():
    # Start from a pretrained YOLO detection model (small is a good beginner choice)
    model = YOLO("yolov8n.pt")

    # Train
    model.train(
        data="data/pv/data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        device=0,  # set to "cpu" if you don't have a GPU
        project="runs",
        name="pv_train",
    )

if __name__ == "__main__":
    main()

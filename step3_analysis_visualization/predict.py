from ultralytics import YOLO
from pathlib import Path

def main():
    weights = "runs/pv_train/weights/best.pt"
    source = "YOUR_IMAGE_OR_FOLDER_HERE"  # e.g. "test_images" or "one_image.jpg"

    model = YOLO(weights)

    results = model.predict(
        source=source,
        conf=0.25,
        save=True,      # saves annotated images
        project="runs",
        name="pv_predict",
    )

    # Print where images are saved
    save_dir = Path(results[0].save_dir)
    print("Saved predictions to:", save_dir)

if __name__ == "__main__":
    main()

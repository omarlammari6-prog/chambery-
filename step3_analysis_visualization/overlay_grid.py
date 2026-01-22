import cv2
from pathlib import Path

def overlay_grid(image_path: str, out_path: str, S: int = 8, thickness: int = 1):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"Could not read: {image_path}")

    h, w = img.shape[:2]

    # Draw vertical lines
    for i in range(1, S):
        x = int(i * w / S)
        cv2.line(img, (x, 0), (x, h), (255, 255, 255), thickness)

    # Draw horizontal lines
    for i in range(1, S):
        y = int(i * h / S)
        cv2.line(img, (0, y), (w, y), (255, 255, 255), thickness)

    cv2.imwrite(out_path, img)
    print("Saved grid overlay to:", out_path)

def main():
    # Change this to your actual prediction image path:
    # Example: runs/pv_predict/your_image.jpg
    pred_img = "PATH_TO_A_PREDICTED_IMAGE.jpg"
    out_img = "PATH_TO_SAVE_WITH_GRID.jpg"

    overlay_grid(pred_img, out_img, S=8, thickness=1)

if __name__ == "__main__":
    main()

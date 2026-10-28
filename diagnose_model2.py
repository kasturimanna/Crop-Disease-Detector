import cv2
from ultralytics import YOLO
import sys

model = YOLO("CropDoctor/models/best.pt")

image_path = "CropDoctor/static/uploads/5c77224c-d02e-4e66-a0eb-5ca782013c55_a9c2119c-b510-4d9b-8ddc-cdb0253e0278___UF.GRC_YLCV_Lab_02287.JPG"
print(f"Testing on image: {image_path}")

img = cv2.imread(image_path)

if img is None:
    print("Could not load image.")
    sys.exit(1)

print("\n--- Confidence 0.25 ---")
results = model.predict(source=img, conf=0.25, verbose=False)
boxes = results[0].boxes
print(f"Detections at 0.25: {len(boxes)}")

print("\n--- Confidence 0.05 ---")
results = model.predict(source=img, conf=0.05, verbose=False)
boxes = results[0].boxes
print(f"Detections at 0.05: {len(boxes)}")
if len(boxes) > 0:
    for box in boxes:
        cls_id = int(box.cls[0])
        cls_name = model.names[cls_id]
        conf = float(box.conf[0])
        print(f"Class: {cls_name}, Conf: {conf:.4f}")

import cv2
from ultralytics import YOLO
import os
import glob

model = YOLO("CropDoctor/models/best.pt")

uploads = glob.glob("CropDoctor/static/uploads/*.*")
for img_path in uploads:
    if not (img_path.endswith('.jpg') or img_path.endswith('.png') or img_path.endswith('.jpeg') or img_path.endswith('.JPG')):
        continue
    img = cv2.imread(img_path)
    if img is None:
        continue
    print(f"\n--- Testing {os.path.basename(img_path)} ---")
    results = model.predict(source=img, conf=0.01, verbose=False)
    boxes = results[0].boxes
    print(f"Detections at 0.01: {len(boxes)}")
    if len(boxes) > 0:
        for box in boxes:
            cls_id = int(box.cls[0])
            cls_name = model.names[cls_id]
            conf = float(box.conf[0])
            print(f"  Class: {cls_name}, Conf: {conf:.4f}")

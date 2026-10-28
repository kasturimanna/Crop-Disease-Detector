from ultralytics import YOLO

model = YOLO("CropDoctor/models/best.pt")

print("Classes:")
print(model.names)

print("Number of classes:")
print(len(model.names))

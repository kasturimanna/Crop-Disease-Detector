import os
import yaml

DATASET_DIR = "PlantDataset_YOLO11"
YAML_PATH = os.path.join(DATASET_DIR, "data.yaml")

def check_classes():
    if not os.path.exists(YAML_PATH):
        print(f"Dataset not found at {DATASET_DIR}. Please place your dataset there to check classes.")
        return

    with open(YAML_PATH, "r") as f:
        data = yaml.safe_load(f)

    classes = data.get("names", [])
    print(f"Total Classes: {len(classes)}")
    
    print("\nClass Names:")
    for i, c in enumerate(classes):
        print(f"  {i}: {c}")

    train_labels = os.path.join(DATASET_DIR, "train", "labels")
    if os.path.exists(train_labels):
        class_counts = {i: 0 for i in range(len(classes))}
        
        for file in os.listdir(train_labels):
            if file.endswith(".txt"):
                with open(os.path.join(train_labels, file), "r") as lf:
                    for line in lf:
                        cls_id = int(line.strip().split()[0])
                        class_counts[cls_id] = class_counts.get(cls_id, 0) + 1
        
        print("\nLabel Counts (Train Set):")
        for i, count in class_counts.items():
            print(f"  {classes[i]}: {count}")
            if count == 0:
                print(f"  [WARNING] Class {classes[i]} has 0 labels!")
    else:
        print("\nTrain labels directory not found to count instances.")

if __name__ == "__main__":
    check_classes()

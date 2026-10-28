import os
import shutil
import yaml
import random
from pathlib import Path
from ultralytics import YOLO

def create_subset(samples_per_class=25, val_per_class=5):
    project_root = Path(__file__).resolve().parent
    dataset_root = project_root.parent / "crop_disease_detection_dataset"
    temp_dir = project_root / "temp_subsample"
    
    if not dataset_root.exists():
        raise FileNotFoundError(f"Dataset not found at {dataset_root}")
        
    # Clean existing temp directory if any
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
        
    for split in ["train", "val"]:
        (temp_dir / split / "images").mkdir(parents=True, exist_ok=True)
        (temp_dir / split / "labels").mkdir(parents=True, exist_ok=True)

    print("[1/3] Reading crop_disease_detection_dataset...")
    class_names = sorted([d.name for d in dataset_root.iterdir() if d.is_dir()])
    print(f"[*] Found {len(class_names)} classes.")
    
    train_count = 0
    val_count = 0
    
    for cls_id, cls_name in enumerate(class_names):
        cls_folder = dataset_root / cls_name
        valid_exts = {".jpg", ".jpeg", ".png", ".JPG"}
        images = [f for f in cls_folder.iterdir() if f.suffix in valid_exts]
        random.seed(42)
        random.shuffle(images)
        
        train_imgs = images[:samples_per_class]
        val_imgs = images[samples_per_class:samples_per_class + val_per_class]
        
        for img_path in train_imgs:
            dest_img = temp_dir / "train" / "images" / img_path.name
            dest_lbl = temp_dir / "train" / "labels" / f"{img_path.stem}.txt"
            shutil.copy2(img_path, dest_img)
            dest_lbl.write_text(f"{cls_id} 0.5 0.5 0.9 0.9\n")
            train_count += 1
            
        for img_path in val_imgs:
            dest_img = temp_dir / "val" / "images" / img_path.name
            dest_lbl = temp_dir / "val" / "labels" / f"{img_path.stem}.txt"
            shutil.copy2(img_path, dest_img)
            dest_lbl.write_text(f"{cls_id} 0.5 0.5 0.9 0.9\n")
            val_count += 1

    print(f"[2/3] Prepared {train_count} training and {val_count} validation samples.")
    
    # Write data.yaml
    temp_yaml_path = temp_dir / "data.yaml"
    temp_yaml_config = {
        "path": str(temp_dir.resolve()),
        "train": "train/images",
        "val": "val/images",
        "nc": len(class_names),
        "names": class_names
    }
    
    with open(temp_yaml_path, "w") as f:
        yaml.safe_dump(temp_yaml_config, f, default_flow_style=False)
        
    return temp_yaml_path

def train():
    project_root = Path(__file__).resolve().parent
    model_output_dir = project_root / "models"
    
    # 1. Prepare dataset subset
    temp_yaml_path = create_subset(samples_per_class=25, val_per_class=5)
    
    # 2. Load YOLO11
    print("[3/3] Loading YOLO11n base weights...")
    model = YOLO("yolo11n.pt")
    
    # 3. Train
    print("[*] Starting local training on CPU (optimized for smooth local execution)...")
    results = model.train(
        data=str(temp_yaml_path),
        epochs=5,
        imgsz=192,
        batch=16,
        device="cpu",
        workers=2,
        project=str(model_output_dir),
        name="cropdoctor_model",
        exist_ok=True,
        verbose=True
    )
    
    best_weights = model_output_dir / "cropdoctor_model" / "weights" / "best.pt"
    final_model = model_output_dir / "best.pt"
    
    if best_weights.exists():
        shutil.copy2(str(best_weights), str(final_model))
        print(f"\n[SUCCESS] New model trained and saved to: {final_model}")
    else:
        print("[WARNING] Could not locate trained best.pt weights.")
        
    # Clean up temporary dataset folder
    try:
        shutil.rmtree(project_root / "temp_subsample")
        print("[*] Temporary subsample folder cleaned.")
    except Exception as e:
        print(f"[*] Note: {e}")

if __name__ == "__main__":
    train()

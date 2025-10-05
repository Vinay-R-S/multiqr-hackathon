# Model Inference script

import os
import json
from ultralytics import YOLO
import torch

MODEL_PATH = "runs/detect/qr_code_detector_cpu2/weights/best.pt"
IMAGES_DIR = "data/images"
OUTPUT_JSON = "output/sample_submission_1.json"

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"🔥 Using device: {device}")

model = YOLO(MODEL_PATH)

image_files = sorted([
    os.path.join(IMAGES_DIR, f)
    for f in os.listdir(IMAGES_DIR)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
])

results_list = []

for img_path in image_files:
    
    print(f"Running inference on: {img_path}")
    result = model.predict(
        source=img_path,
        device=device,
        verbose=False
    )[0]

    # Extract bounding boxes (x1, y1, x2, y2)
    boxes = result.boxes.xyxy.cpu().numpy().tolist() if result.boxes is not None else []
    image_id = os.path.splitext(os.path.basename(img_path))[0]

    qrs_list = [{"bbox": [float(x1), float(y1), float(x2), float(y2)]} for x1, y1, x2, y2 in boxes]

    results_list.append({
        "image_id": image_id,
        "qrs": qrs_list
    })

with open(OUTPUT_JSON, "w") as f:
    json.dump(results_list, f, indent=2)

print(f"\nInference complete! Output saved to → {OUTPUT_JSON}")

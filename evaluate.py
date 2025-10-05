# Model evaluation script

import os
import json
import numpy as np
from PIL import Image

PRED_JSON = "output/sample_submission_1.json"
LABELS_DIR = "data/labels"
IMAGES_DIR = "data/images"

IOU_THRESHOLD = 0.5

def yolo_to_xyxy(yolo_boxes, img_w, img_h):
    """Convert YOLO normalized (cx, cy, w, h) → (x1, y1, x2, y2)."""
    boxes = []
    for box in yolo_boxes:
        _, cx, cy, w, h = box
        x1 = (cx - w / 2) * img_w
        y1 = (cy - h / 2) * img_h
        x2 = (cx + w / 2) * img_w
        y2 = (cy + h / 2) * img_h
        boxes.append([x1, y1, x2, y2])
    return np.array(boxes)

def iou(box1, box2):
    """Compute IoU between two boxes [x1, y1, x2, y2]."""
    xA = max(box1[0], box2[0])
    yA = max(box1[1], box2[1])
    xB = min(box1[2], box2[2])
    yB = min(box1[3], box2[3])
    inter = max(0, xB - xA) * max(0, yB - yA)
    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    return inter / (area1 + area2 - inter + 1e-6)

with open(PRED_JSON, "r") as f:
    predictions = json.load(f)

ious = []
true_positives = 0
false_positives = 0
false_negatives = 0

for entry in predictions:
    image_id = entry["image_id"]
    pred_boxes = np.array([qr["bbox"] for qr in entry["qrs"]])
    
    label_path = os.path.join(LABELS_DIR, image_id + ".txt")
    img_path = os.path.join(IMAGES_DIR, image_id + ".jpg")
    
    if not os.path.exists(label_path):
        print(f"⚠️ No label for {image_id}, skipping.")
        continue

    # Get image size to convert YOLO boxes
    with Image.open(img_path) as img:
        w, h = img.size

    gt_yolo_boxes = np.loadtxt(label_path).reshape(-1, 5)
    gt_boxes = yolo_to_xyxy(gt_yolo_boxes, w, h)

    matched_gt = set()
    for pb in pred_boxes:
        best_iou = 0
        best_gt_idx = -1
        for i, gt in enumerate(gt_boxes):
            current_iou = iou(pb, gt)
            if current_iou > best_iou:
                best_iou = current_iou
                best_gt_idx = i
        ious.append(best_iou)
        if best_iou >= IOU_THRESHOLD:
            true_positives += 1
            matched_gt.add(best_gt_idx)
        else:
            false_positives += 1

    false_negatives += len(gt_boxes) - len(matched_gt)

mean_iou = np.mean(ious) if ious else 0
precision = true_positives / (true_positives + false_positives + 1e-6)
recall = true_positives / (true_positives + false_negatives + 1e-6)
f1 = 2 * precision * recall / (precision + recall + 1e-6)

print("\nEvaluation Results:")
print(f"Mean IoU: {mean_iou:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"True Positives: {true_positives}")
print(f"False Positives: {false_positives}")
print(f"False Negatives: {false_negatives}")

# multiqr-hackathon
DL model to detect the QR codes and get the data and classify it based on the contents of it

## Problem Statement  
This hackathon is about solving a real problem in the medical field – **recognizing multiple QR codes on medicine packs**.  
Most medicine packs have more than one QR code, such as codes for the **manufacturer, batch number, distributor, or regulator**. The challenge is to **detect all these QR codes from an image**. For advanced participants, an additional bonus challenge is to **decode the QR contents and classify them**.  


## Dataset  
[Dataset](https://drive.google.com/file/d/1YCQggB6DdBEeIeBJy_odCW8ma_dq6Fg9/view)
- You will be given a dataset of **200 medicine pack images** with annotated QR bounding boxes.  
- These will help you **train and validate** your models for the main detection task.  
- A **test set of 50 images** will be used for final scoring, which also contains decoded QR values for bonus evaluation.  
- Additional hidden images will also be used to validate accuracy and benchmarking.  

## Project structrure 
```
multiqr-hackathon/
│
├── ProblemStatement.md
├── README.md                                # Setup & usage instructions
├── requirements.txt                         # Python dependencies
├── train.py                                 # Training script
├── infer.py                                 # Must implement inference (input=images → output=JSON)
├── evaluate.py                              # (Optional) for self-check with provided GT
│
├── data/   
│   ├── images                               # (participants don't commit dataset, only placeholder)
│   └── labels/                              # You’ll provide a small demo set
│
├── outputs/                       
│   ├── submission_detection_1.json          # Required output file (Stage 1)
│   └── submission_decoding_2.json           # Required output file (Stage 2, bonus)
│
└── src/                          
    ├── models/                              # Model weights (PyTorch models so .pt extension)
    |   ├── yolov8n.pt
    |   └── yolov8s.pt
    ├── annotated_augmented_dataset/         # Dataset is stored here loading & preprocessing
    |   ├── train
    |   |   ├── images
    |   |   └── labels
    |   ├── valid
    |   |   ├── images
    |   |   └── labels
    |   └── data.yaml
    ├── datasets/                            # Customm Dataset downloaded from the Google drive
    └── script/                              # Python Scripts to run any processes
        └── rename_dataset.py
```

`Note: YOLOv8 model needs validation set while traning and testing so the test set is used as valid set testing can be done on external images`

## Run the project in this manner

`Step 1:` Set the virtual environment [Run the below commands]
```
python -m venv .venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

`Step 2:` Download the dataset form the above link <br>
`Step 3:` Annotate the images using [roboflow](https://app.roboflow.com/) to add the bouding box <br>
`Step 4:` Use the Preprocessing and Augmentation option while versioning the dataset and download the annotated dataset inside `annotated_augmented_dataset` folder. <br>
`Step 5:` Copy some images and their labels from test folder and store in data folder to get the inference of the images & rename the test folder as valid since yolov8 uses valid as testing internally<br>
`Step 6:` Run the `main.py` by using this command `python .\main.py` it will run the below python scripts in the order <br>
 ├── `Sub-Step 1:` Rename python script to get the clear and common naming format for images `python .\src\script\rename_dataset.py` <br>
 ├── `Sub-Step 2:` Start the traning process by running this command `python .\train.py` <br>
 ├── `Sub-Step 3:` Run the inference file `python .\infer.py` to get the inference <br>
 └── `Sub-Step 4:` Run the evaluate file to get the model performace details `python .\evaluate` <br>

## Results
```
Evaluation Results:
Mean IoU: 0.8500 (85% accuracy its union of QR area of predicted and real QR area)
Precision: 1.0000
Recall: 1.0000
F1 Score: 1.0000
True Positives: 29
False Positives: 0
False Negatives: 0
```

# Training Metrics

## Training Metrics per Epoch

| Epoch  | GPU_mem | box_loss | cls_loss | dfl_loss | Instances | Size | Box(P) | R     | mAP50 | mAP50-95 |
|--------|---------|----------|----------|----------|-----------|------|--------|-------|-------|----------|
| 1/30   | 0G      | 1.879    | 2.122    | 1.393    | 6         | 640  | 0.775  | 0.855 | 0.818 | 0.393    |
| 5/30   | 0G      | 1.456    | 0.9304   | 1.189    | 6         | 640  | 0.891  | 0.921 | 0.829 | 0.524    |
| 10/30  | 0G      | 1.376    | 0.7205   | 1.150    | 20        | 640  | 0.894  | 0.915 | 0.840 | 0.503    |
| 15/30  | 0G      | 1.319    | 0.6614   | 1.125    | 8         | 640  | 0.895  | 0.912 | 0.861 | 0.577    |
| 20/30  | 0G      | 1.267    | 0.5947   | 1.110    | 14        | 640  | 0.878  | 0.915 | 0.838 | 0.547    |
| 25/30  | 0G      | 1.177    | 0.5322   | 1.090    | 9         | 670  | 0.899  | 0.915 | 0.861 | 0.581    |
| 30/30  | 0G      | 1.113    | 0.487    | 1.057    | 5         | 640  | 0.904  | 0.915 | 0.867 | 0.592    |

## Validation Metrics

| Class | Images | Instances | Box(P) | R     | mAP50 | mAP50-95 |
|-------|--------|-----------|--------|-------|-------|----------|
| all   | 50     | 177       | -      | -     | -     | -        |


### Notes
- The "Instances" column under training refers to the number of instances per batch.
- Validation metrics (Box(P), R, mAP50, mAP50-95) are reported for the entire validation set after each epoch.
- GPU memory usage is consistently 0G, indicating no GPU was used or detected.


## Sample submission in `output folder` - The bounding box co-ordinates after the inference

## Project is divided into 2 stages

### Stage 1: Detection

- **File name**: `submission_detection_1.json`  
- **Task**: Submit bounding boxes of detected QR codes.  

### Format:
```json
[
  {
    "image_id": "img001",
    "qrs": [
      { "bbox": [50, 30, 120, 100] },
      { "bbox": [200, 80, 260, 140] }
    ]
  }
]
```

### Stage 2 (Bonus): Decoding + Classification

- **File name:** submission_decoding_2.json (fixed name)
- **Task:** Submit bounding boxes along with decoded QR values and types.
- **Eligibility:** Only for teams that pass the Stage 1 threshold.

### Format:
```json
[
  {
    "image_id": "img001",
    "qrs": [
      { "bbox": [50, 30, 120, 100], "value": "B12345" },
      { "bbox": [200, 80, 260, 140], "value": "MFR56789" }
    ]
  }
]
```
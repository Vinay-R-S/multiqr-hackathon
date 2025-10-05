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
├── data/                                    # (participants don't commit dataset, only placeholder)
│   └── demo_images/                         # You’ll provide a small demo set
│
├── outputs/                       
│   ├── submission_detection_1.json          # Required output file (Stage 1)
│   └── submission_decoding_2.json           # Required output file (Stage 2, bonus)
│
└── src/                          
    ├── models/                              # Model definitions
    |   ├── yolov8n.pt
    |   ├── yolov8s.pt
    ├── annotated_augmented_dataset/         # Dataset loading & preprocessing
    |   ├── train
    |   |   ├── images
    |   |   ├── labels
    |   ├── valid
    |   |   ├── images
    |   |   ├── labels
    |   └──data.yaml
    ├── datasets/                            # Dataset loading & preprocessing
    ├── script/                              # Dataset loading & preprocessing
    |   └── rename_dataset.py
    ├── utils/                               # Utility functions
    └── __init__.py
```

`Note: YOLOv8 model needs validation set while traning and testing so the test set is used as valid set testing can be done on external images`

## Run the project in this manner

`Step 1:` Set the virtual environment [Run the below commands]
```
python -m venv .venv
.\venv\Scripts\activate
```
`Step 2:` Download the dataset form the above link <br>
`Step 3:` Annotate the images using [roboflow](https://app.roboflow.com/) to add the bouding box <br>
`Step 4:` Use the Preprocessing and Augmentation option while versioning the dataset and download the annotated dataset inside `annotated_augmented_dataset` folder. <br>
`Step 5:` Run the rename python script to get the clear and common naming format for images
`python .\src\script\rename_dataset.py` and rename test folder as valid since yolov8 uses valid as testing internally<br>
`Step 6:` Start the traning process by running this command `python .\train.py` <br>
`Step 7:` Copy some images and their labels from valid folder and store in data folder to get the inference of the images
`Step 7:` Run the inference file `python .\infer.py` to get the inference
`Step 8:` Run the evaluate file to get the model performace details `python .\evaluate`

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
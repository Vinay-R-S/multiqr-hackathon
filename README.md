# multiqr-hackathon
DL model to detect the QR codes and get the data and classify it based on the contents of it

## Problem Statement  
This hackathon is about solving a real problem in the medical field – **recognizing multiple QR codes on medicine packs**.  
Most medicine packs have more than one QR code, such as codes for the **manufacturer, batch number, distributor, or regulator**. The challenge is to **detect all these QR codes from an image**. For advanced participants, an additional bonus challenge is to **decode the QR contents and classify them**.  


## Dataset  
![Dataset](https://drive.google.com/file/d/1YCQggB6DdBEeIeBJy_odCW8ma_dq6Fg9/view)
- You will be given a dataset of **200 medicine pack images** with annotated QR bounding boxes.  
- These will help you **train and validate** your models for the main detection task.  
- A **test set of 50 images** will be used for final scoring, which also contains decoded QR values for bonus evaluation.  
- Additional hidden images will also be used to validate accuracy and benchmarking.  

## Project structrure 
```
multiqr-hackathon/
│
├── ProblemStatement.md
├── README.md                      # Setup & usage instructions
├── requirements.txt               # Python dependencies
├── train.py                       # Training script
├── infer.py                       # Must implement inference (input=images → output=JSON)
├── evaluate.py                    # (Optional) for self-check with provided GT
│
├── data/                          # (participants don't commit dataset, only placeholder)
│   └── demo_images/               # You’ll provide a small demo set
│
├── outputs/                       
│   ├── submission_detection_1.json   # Required output file (Stage 1)
│   └── submission_decoding_2.json    # Required output file (Stage 2, bonus)
│
└── src/                          
    ├── models/                    # Model definitions
    ├── datasets/                  # Dataset loading & preprocessing
    ├── utils/                     # Utility functions
    └── __init__.py
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
      { "bbox": [x_min, y_min, x_max, y_max] },
      { "bbox": [x_min, y_min, x_max, y_max] }
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
      { "bbox": [x_min, y_min, x_max, y_max], "value": "B12345" },
      { "bbox": [x_min, y_min, x_max, y_max], "value": "MFR56789" }
    ]
  }
]
```
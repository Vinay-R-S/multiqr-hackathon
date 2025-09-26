# Multi-QR Code Recognition for Medicine Packs

## Problem Statement  
This hackathon is about solving a real problem in the medical field – **recognizing multiple QR codes on medicine packs**.  
Most medicine packs have more than one QR code, such as codes for the **manufacturer, batch number, distributor, or regulator**. The challenge is to **detect all these QR codes from an image**. For advanced participants, an additional bonus challenge is to **decode the QR contents and classify them**.  


## Dataset  
![Dataset](https://drive.google.com/file/d/1YCQggB6DdBEeIeBJy_odCW8ma_dq6Fg9/view)
- You will be given a dataset of **200 medicine pack images** with annotated QR bounding boxes.  
- These will help you **train and validate** your models for the main detection task.  
- A **test set of 50 images** will be used for final scoring, which also contains decoded QR values for bonus evaluation.  
- Additional hidden images will also be used to validate accuracy and benchmarking.  


## What Needs to be Done  
- The submitted code must be **complete, runnable, and reproducible**.  
- **Detect all QR codes** in the provided images using the bounding box annotations for training.  
- Ensure detection works even with **tilted, blurred, or partially covered images**.  
- For those achieving strong detection performance, attempt the **bonus task** of decoding and classifying the QR codes on the test set.  


## What Makes it Competitive  
- **Main challenge**: QR detection – all participants compete on the same dataset.  
- **Bonus challenge**: QR decoding and classification – available only after demonstrating strong detection accuracy.  
- Dataset includes realistic variations such as **lighting, tilt, and occlusion**.  
- Extra credit for **efficient solutions** (lighter, faster models rank higher in case of ties).  


## Summary  
- **Main Task** → Detect all QR codes in medicine pack images.  
- **Bonus Task** → Decode and classify QR codes.  
- **Evaluation** → Based on detection accuracy, robustness, efficiency, and bonus classification performance.  


## Evaluation Plan

## Restrictions  
- **Do not use any external APIs** (including QR code reading/decoding APIs) at any stage for generating results.  
- The submitted code must be **complete, runnable, and reproducible**.  

Organizers should be able to:  
1. Clone/unzip your repository.  
2. Follow the README instructions.  
3. Run a **single command** to reproduce your output on the given images.  


## Scoring

### 1. Decoding & Classification Score (Bonus Task)  
- **Metric:** String accuracy of decoded QR values + correct classification type.  
- **Weight:** Added bonus on hidden **50 images only**.  

### 2. Final Score Composition  
- Participants train and test on the provided **200 images**.  
- They must submit:  
  - `submission_detection_1.json` → JSON file for the **test 50 images**.  
  - **Complete runnable code + README**.  

- Organizers will then run the submitted code on **50 hidden images** (not shared with participants) to evaluate:  
  - **Detection** (mandatory).  
  - **Decoding & Classification** (bonus).  

- **Winners** will be decided based on **hidden test performance**.  

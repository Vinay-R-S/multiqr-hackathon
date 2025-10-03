# Model traning script

from ultralytics import YOLO
import os

def train_qr_code_detector():
    """
    Downloads a pre-trained YOLOv8 model and fine-tunes it on the QR code dataset.
    This version is optimized for CPU training with parallel processing.
    """
    # ----------------------------------------------------------------------
    # 1. Define Paths (ADJUSTED FOR SCRIPT IN PROJECT ROOT)
    # The script is in the project root, so the path is relative to the root.
    # ----------------------------------------------------------------------
    
    # Path to the data configuration file: 'src/annotated_augmented_dataset/data.yaml'
    DATA_YAML_PATH = 'src/annotated_augmented_dataset/data.yaml'
    
    # Check if the YAML file exists before starting
    if not os.path.exists(DATA_YAML_PATH):
        print(f"Error: Data YAML file not found at {os.path.abspath(DATA_YAML_PATH)}")
        print("Please ensure 'data.yaml' is in the 'src/annotated_augmented_dataset' folder.")
        return

    # ----------------------------------------------------------------------
    # 2. Model Loading Check (Retained for a quick check)
    # ----------------------------------------------------------------------
    try:
        # We load the fast, nano model 'yolov8n.pt' for CPU training.
        print("Loading pre-trained YOLOv8s model for initial check...")
        _ = YOLO('yolov8s.pt') 
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Please ensure you have installed the ultralytics package: pip install ultralytics")
        return

    # ----------------------------------------------------------------------
    # 3. Train the Model (Optimized for CPU with Parallel Processing)
    # ----------------------------------------------------------------------
    print(f"Starting training on data defined in: {DATA_YAML_PATH}")
    print("CPU detected: Using device='cpu', smaller batch size (4), yolov8n model, and 8 workers for parallel data loading.")
    
    # Load the Nano model for faster CPU processing
    model = YOLO('yolov8n.pt')
    
    # Setting the number of workers to utilize 8 CPU cores for faster data loading
    NUM_WORKERS = 8 

    # Start training! The results will be saved in a 'runs/detect/trainX' directory.
    # NOTE: The YAML file will handle using the 'test' data for validation (val).
    results = model.train(
        data=DATA_YAML_PATH,        # Corrected Path to the data configuration file
        epochs=30,                  
        imgsz=640,                  
        batch=4,                    # REDUCED batch size for CPU memory limits
        device='cpu',               # Explicitly force CPU usage
        workers=NUM_WORKERS,        # Utilizes 8 CPU cores for parallel data loading
        name='qr_code_detector_cpu' # Name for the resulting run folder
    )

    print("\n--- Training Complete ---")
    print("Results and best weights saved in: runs/detect/qr_code_detector_cpu")

if __name__ == '__main__':
    train_qr_code_detector()

import os
import re
from typing import List, Dict

def process_split(root_path: str, split_name: str):
    """
    Processes a single dataset split (e.g., 'train' or 'test') by first building 
    a consistent mapping from image files and then applying it to both images and labels.
    """
    images_path: str = os.path.join(root_path, split_name, 'images')
    labels_path: str = os.path.join(root_path, split_name, 'labels')
    
    # Check if the expected images directory exists
    if not os.path.isdir(images_path):
        # We also need to check if the root path itself is incorrect before printing skip messages
        if not os.path.isdir(os.path.join(root_path, split_name)):
            print(f"  Skipping {split_name}: Base split directory not found at {os.path.join(root_path, split_name)}")
        else:
            print(f"  Skipping {split_name}: Images directory not found at {images_path}")
        return

    # Regex to capture the base name 'imgXXX' and the full filename without extension
    # Group 1: (img\d+) e.g., 'img001'
    # Group 2: (.*) e.g., '_jpg.rf.5a4d2b4dbd13c5b744f1bec9ffa995aa'
    filename_parts_pattern = re.compile(r'(img\d+)(.*)\.(jpg|txt)$')

    # 1. BUILD MAPPING: Scan the images folder to create a name transformation map.
    # This ensures consistency across images and labels.
    print(f"\nBuilding mapping for {split_name}...")
    
    # map: { original_full_name_without_ext: new_name_without_ext }
    rename_map: Dict[str, str] = {}
    base_name_counts: Dict[str, int] = {} # Counts for 'img001', 'img002', etc.

    # We sort the image files to ensure deterministic numbering (img001_1, img001_2, ...)
    image_files: List[str] = sorted(os.listdir(images_path))
    
    for filename in image_files:
        match = filename_parts_pattern.match(filename)
        
        # Only process files that match the expected pattern and are images
        if not match or match.group(3) != 'jpg':
            continue

        base_name: str = match.group(1) # e.g., 'img001'
        original_stem: str = os.path.splitext(filename)[0] # Full original name without .jpg

        # Increment counter for this original image group
        base_name_counts[base_name] = base_name_counts.get(base_name, 0) + 1
        counter: int = base_name_counts[base_name]

        # New format: imgXXX_N (e.g., 'img001_1')
        new_stem: str = f"{base_name}_{counter}"
        
        # Store the mapping for later use on both .jpg and .txt
        rename_map[original_stem] = new_stem
        
    print(f"  Mapping built for {len(rename_map)} unique augmented files.")


    # 2. APPLY MAPPING: Apply the collected map to both images and labels directories.
    
    def apply_rename(directory: str, file_type: str):
        """Helper to execute renames in a given directory."""
        if not os.path.isdir(directory):
            print(f"  Warning: Directory not found: {directory}. Skipping.")
            return 0
            
        count_executed = 0
        current_files = os.listdir(directory)
        
        for filename in current_files:
            if not filename.endswith(f'.{file_type}'):
                continue
            
            original_stem: str = os.path.splitext(filename)[0] # Full original name without extension
            
            if original_stem in rename_map:
                new_stem: str = rename_map[original_stem]
                new_filename: str = f"{new_stem}.{file_type}"
                
                old_filepath: str = os.path.join(directory, filename)
                new_filepath: str = os.path.join(directory, new_filename)
                
                try:
                    # Rename the file in-place
                    os.rename(old_filepath, new_filepath)
                    count_executed += 1
                except OSError as e:
                    print(f"  Error renaming {filename} to {new_filename}: {e}")
        
        return count_executed

    # Apply to images
    img_count = apply_rename(images_path, 'jpg')
    print(f"  --> Successfully renamed {img_count} images in {split_name}/images.")

    # Apply to labels
    txt_count = apply_rename(labels_path, 'txt')
    print(f"  --> Successfully renamed {txt_count} labels in {split_name}/labels.")


def rename_dataset_files(base_dir: str):
    """
    Orchestrates the renaming process for 'train' and 'test' splits.
    """
    
    print(f"--- Starting Consistent Renaming Process in: {os.path.abspath(base_dir)} ---")

    process_split(base_dir, 'train')
    process_split(base_dir, 'test')
        
    print("\nFile renaming complete! Image and label pairings are preserved.")

if __name__ == '__main__':
    # --- Set the path to your dataset root folder ---
    # The path is adjusted to include 'src/' based on the user's directory structure image.
    DATASET_ROOT = 'src/annotated_augmented_dataset'
    rename_dataset_files(DATASET_ROOT)

import os
import shutil
import random

# Set up the paths
source_folder = "/home/nvidia/on_fire_project/notOnFire"
train_folder = "/home/nvidia/on_fire_project/train/notOnFire"
val_folder = "/home/nvidia/on_fire_project/val/notOnFire"
test_folder = "/home/nvidia/on_fire_project/test/notOnFire"

# Create destination folders if they don't exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Get the list of image filenames
image_files = [f'image{i}.jpg' for i in range(1, 487)]

# Shuffle the image files
random.shuffle(image_files)

# Calculate the number of images for each split
total_images = len(image_files)
train_count = int(total_images * 0.7)
val_count = int(total_images * 0.15)

# Copy images to their respective folders
for idx, image_file in enumerate(image_files):
    source_path = os.path.join(source_folder, image_file)
    
    if idx < train_count:
        destination_path = os.path.join(train_folder, image_file)
    elif idx < train_count + val_count:
        destination_path = os.path.join(val_folder, image_file)
    else:
        destination_path = os.path.join(test_folder, image_file)
    
    shutil.copy(source_path, destination_path)

print("Images sorted into train, val, and test folders.")

import cv2
import os
import numpy as np

def apply_clahe(image):
    # Calculate the clip limit based on the image content
    clip_limit = np.mean(cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2))

    # Apply CLAHE with the calculated clip limit
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(8, 8))
    image = clahe.apply(image)
    return image

# Set the paths for the input and output folders
input_folder = "C:/path/to/input/folder"
output_folder = "C:/path/to/output/folder"

# Create the output folder if it does not exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is an image (you can add more file extensions if needed)
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Read the image
        img = cv2.imread(os.path.join(input_folder, filename), 0)

        # Apply CLAHE to the image
        ahe_img = apply_clahe(img)

        # Save the enhanced image to the output folder with the same filename
        cv2.imwrite(os.path.join(output_folder, filename), ahe_img)

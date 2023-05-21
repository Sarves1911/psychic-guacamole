import cv2
import os

def apply_ahe(image):
    # Apply AHE to the image
    image = cv2.equalizeHist(image)
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
        img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_GRAYSCALE)

        # Apply AHE to the image
        ahe_img = apply_ahe(img)

        # Save the enhanced image to the output folder with the same filename
        cv2.imwrite(os.path.join(output_folder, filename), ahe_img)

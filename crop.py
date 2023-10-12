import os
import cv2

# Specify the folder containing your images
folder_path = '0'

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):  # Add more extensions if needed
        file_path = os.path.join(folder_path, filename)

        # Read the image using OpenCV
        image = cv2.imread(file_path)

        # Get the height and width of the image
        height, width = image.shape[:2]

        # Crop the top 50 pixels and the bottom 50 pixels
        cropped_image = image[60:height-60, :]

        # Save the cropped image back to the original file
        cv2.imwrite(file_path, cropped_image)

print("Cropping complete. Original images in the folder have been updated.")
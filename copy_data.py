import os
import shutil

# Specify the folder containing the images
source_folder = '0'

# Specify the number of copies you want to make (including decimal values)
num_copies = 1.18  # Change this to the desired number of copies

# List all files in the source folder
files = os.listdir(source_folder)

# Filter for image files (you can adjust this if needed)
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]

# Calculate the integer and fractional parts of num_copies
int_copies = int(num_copies)
frac_copies = num_copies - int_copies

# Make integer copies
for i in range(int_copies):
    for image in image_files:
        source_path = os.path.join(source_folder, image)
        new_name = os.path.splitext(image)[0] + f'_copy{i+1}' + os.path.splitext(image)[1]
        destination_path = os.path.join(source_folder, new_name)
        shutil.copy(source_path, destination_path)

# Make fractional copies for a portion of the images
if frac_copies > 0:
    num_images_to_copy = int(len(image_files) * frac_copies)
    images_to_copy = image_files[:num_images_to_copy]

    for image in images_to_copy:
        source_path = os.path.join(source_folder, image)
        new_name = os.path.splitext(image)[0] + f'_copy{int_copies + 1}' + os.path.splitext(image)[1]
        destination_path = os.path.join(source_folder, new_name)
        shutil.copy(source_path, destination_path)

print(f'{num_copies} copies of image files have been created in the folder.')

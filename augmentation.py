import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# Path to your dataset folder
data_folder = '1'

# Path to the folder where augmented images will be saved
output_folder = '1A'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Initialize the ImageDataGenerator with desired augmentations
datagen = ImageDataGenerator(
    rotation_range=5,
    shear_range=0.2,
    width_shift_range=0.05,
    height_shift_range=0.05,
    zoom_range=0.1,
    brightness_range=[0.8, 1.2],
    horizontal_flip=True,
    fill_mode='nearest')

# List all files in the data folder
file_list = os.listdir(data_folder)

# Number of times to augment each image
augmentation_factor = 2

# Loop through each image and apply augmentation
count=0
for file in file_list:
    img = load_img(os.path.join(data_folder, file))
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    i = 0
    for batch in datagen.flow(x, batch_size=1):
        augmented_image = array_to_img(batch[0])
        augmented_image.save(os.path.join(output_folder, f'{file.split(".")[0]}_{i}.jpg'))  # Save augmented image
        i += 1
        count+=1
        if i >= augmentation_factor:
            break  # Break the loop if we've reached the desired number of augmentations
        if count>1500:
            break

print("Image augmentation complete.")

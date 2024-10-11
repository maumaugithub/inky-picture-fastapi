from PIL import Image
import os

def resize_pic(image_path, output_folder, size=(800, 800)):
    # Open an image file
    with Image.open(image_path) as img:
        # Resize image
        img.thumbnail(size)
        # Save it to the output folder
        base_name = os.path.basename(image_path)
        resized_image_path = os.path.join(output_folder, base_name)
        img.save(resized_image_path)
        return resized_image_path
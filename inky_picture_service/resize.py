from PIL import Image
import os
from pathlib import Path


def resize_pic(image_path, resize_folder=None, size=(800, 800)):
    # Open an image file
    with Image.open(image_path) as img:
        if img.size == size:
            return image_path
        print(f'Original size: {img.size}')
        # Resize image
        img.thumbnail(size)
        print(f'Resizing to {size[0]}x{size[1]} pixels')
        # Create a new path for resized file
        file_name = os.path.splitext(image_path)   
        base_name = os.path.basename(image_path)
        original_path = str(os.path.abspath(image_path)).rstrip(f'{base_name}{file_name[1]}')
        if resize_folder:
            Path(f'{original_path}{resize_folder}').mkdir(parents=True, exist_ok=True)
        new_res_path = f'{original_path}{resize_folder}\\{base_name.
            rstrip(file_name[1])}-{size[0]}x{size[1]}{file_name[1]}' if resize_folder else f'{original_path}{base_name.
            rstrip(file_name[1])}-{size[0]}x{size[1]}{file_name[1]}'
        print(new_res_path)
        # Save it to the output folder
        img.save(new_res_path)
        return new_res_path

# # Resize image in AREPL
# pic_path = Path("../test/asset/cacti-hi.jpg")
# resized_image_path = resize_pic(pic_path, "resize")
# print(resized_image_path)

import os
from PIL import Image

input_directory = "/content/sample_data/test"

for filename in os.listdir(input_directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):  
        img_path = os.path.join(input_directory, filename)
        img = Image.open(img_path)
        rotated_img = img.rotate(90, expand=True) 
        output_path = os.path.join(input_directory, f"{filename[:-4]}_rotated.jpg")
        rotated_img.save(output_path)
        img = Image.open(output_path)
        rotated_img = img.rotate(90, expand=True) 
        output_path = os.path.join(input_directory, f"{filename[:-4]}_rotated1.jpg")
        rotated_img.save(output_path)
        img = Image.open(output_path)
        rotated_img = img.rotate(90, expand=True)
        output_path = os.path.join(input_directory, f"{filename[:-4]}_rotated2.jpg")
        rotated_img.save(output_path)

print("Rotation completed.")
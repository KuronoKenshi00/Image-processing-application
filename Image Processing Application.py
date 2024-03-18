from PIL import Image, ImageOps, ImageFilter
import os
import numpy as np
from sklearn.cluster import KMeans
import time

def open_image(file_path):
    try:
        image = Image.open(file_path)
        return image
    except IOError:
        print("Unable to open  the image")
        return None

def save_image(image, output_folder, file_name, file_format=None):
    try:
        os.makedirs(output_folder, exist_ok= True)
        output_path = os.path.join(output_folder, file_name)
        image.save(output_path, format=file_format)
        print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

def resize_image(image, width, height):
    resized_image = image.resize((width,height))
    return resized_image

def apply_filter(image, filter_type):
    filtered_image = image.filter(filter_type)
    return filtered_image

def equalize_image(image):
    equalized_image = ImageOps.equalize(image)
    return equalized_image

def generate_unique_filename(base_name, file_format):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    return f"{base_name}_{timestamp}.{file_format.lower()}"

def main():
    file_path = input("Enter the path to the image file: ")
    print(f"File path provided: {file_path}")
    output_folder1 = R"C:/Users/Prashanth/Desktop/Nexilo Tech Py/Task 1/Resized Image"
    output_folder2 = R"C:/Users/Prashanth/Desktop/Nexilo Tech Py/Task 1/Blurred Image"
    output_folder3 = R"C:/Users/Prashanth/Desktop/Nexilo Tech Py/Task 1/Equalized Image"

    file_name_resized = generate_unique_filename("resized_image", "jpg")
    file_name_blurred = generate_unique_filename("blurred_image", "jpg")
    file_name_equalized = generate_unique_filename("equalized_image", "jpg")
    width = 300
    height = 300

    #open the image
    original_image = open_image(file_path)
    if original_image is None:
        return

    #Perform image processing
    resized_image = resize_image(original_image, width, height)
    blurred_image = apply_filter(original_image, ImageFilter.BLUR)
    equalized_image = equalize_image(original_image)

    #save the processed image
    save_image(resized_image, output_folder1, file_name_resized, file_format="JPEG")
    save_image(blurred_image, output_folder2, file_name_blurred, file_format="JPEG")
    save_image(equalized_image, output_folder3, file_name_equalized, file_format="JPEG")

if __name__ == "__main__":
    main()
    
    
    
    

import cv2 
import os
import numpy as np
from pdf2image import convert_from_path

file_path = "image"
output = "converted_image"

poppler_path = r"poppler-24.08.0\Library\bin"

os.makedirs(output, exist_ok=True)

for filename in os.listdir(file_path):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(file_path, filename)

        images = convert_from_path(pdf_path, poppler_path=poppler_path)

        for page_num, image in enumerate(images):
            image = image.convert("RGB")
            image_np = np.array(image)

            image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

            output_filename = f"{os.path.splitext(filename)[0]}_page_{page_num + 1}.jpg"
            output_path = os.path.join(output, output_filename)

            cv2.imwrite(output_path, image_np)
            print(f"saved {output_path}")

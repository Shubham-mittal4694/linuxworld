
#!/usr/bin/env python3

import cgi
import cgitb
import json
import os
import uuid
from PIL import Image, ImageFilter

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers including CORS headers
print("Content-Type: application/json")
print("Access-Control-Allow-Origin: *")  # Allow requests from any origin (you can restrict it as needed)
print()  # Blank line required between headers and body

def blur_image(image_file):
    try:
        # Open the uploaded image
        image = Image.open(image_file)

        # Apply a Gaussian blur filter
        blurred_image = image.filter(ImageFilter.GaussianBlur(5))

        blurred_image_filename = str(uuid.uuid4()) + ".jpg"
        save_directory = './blurred_images/'

        if not os.path.exists(save_directory):
            os.makedirs(save_directory)

        blurred_image_path = os.path.join(save_directory, blurred_image_filename)
        blurred_image.save(blurred_image_path)

        return {"status": "success", "blurred_image_path": blurred_image_path}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

# Process the uploaded image
form = cgi.FieldStorage()
if "image" in form:
    image_file = form["image"]
    if image_file.filename:  # Check if file was uploaded
        result = blur_image(image_file.file)
    else:
        result = {"status": "failed", "error": "No image file uploaded"}
else:
    result = {"status": "failed", "error": "No image file provided"}

# Output the result as JSON
print(json.dumps(result))

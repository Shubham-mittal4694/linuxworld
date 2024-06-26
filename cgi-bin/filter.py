#!/usr/bin/env python3

import cgi
import cgitb
import os
import cv2
import numpy as np

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: text/html\n")

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get the uploaded file
fileitem = form['file']

def apply_filter(image_path):
    try:
        # Read the image
        img = cv2.imread(image_path)
        
        # Apply a simple blur filter
        filtered_img = cv2.GaussianBlur(img, (15, 15), 0)
        
        # Define path to save the filtered image
        filtered_image_path = '/tmp/filtered_image.jpg'
        
        # Save the filtered image
        cv2.imwrite(filtered_image_path, filtered_img)
        
        return filtered_image_path
    except Exception as e:
        return str(e)

result = "No file uploaded."

if fileitem.filename:
    # Define a path to store the uploaded file temporarily
    filepath = os.path.join('/tmp', os.path.basename(fileitem.filename))
    
    # Save the uploaded file to the temporary path
    with open(filepath, 'wb') as f:
        f.write(fileitem.file.read())
    
    # Apply filter to the uploaded image
    filtered_image_path = apply_filter(filepath)
    
    # Provide the result link
    result = f"Filtered image saved at: {filtered_image_path}"

print(f"<html><body><h1>{result}</h1></body></html>")

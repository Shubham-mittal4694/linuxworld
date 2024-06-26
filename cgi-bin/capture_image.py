#!/usr/bin/env python3

import cgi
import cgitb
import base64

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers including CORS headers
print("Content-Type: text/plain")
print("Access-Control-Allow-Origin: *")  # Adjust origin as needed
print()

# Parse the form data
form = cgi.FieldStorage()

# Check if the form contains image data
if "imageData" in form:
    # Retrieve the base64-encoded image data
    imageData = form["imageData"].value

    # Remove the prefix 'data:image/jpeg;base64,' before decoding
    imageData = imageData.replace('data:image/jpeg;base64,', '')

    try:
        # Decode base64 string to bytes
        imageBytes = base64.b64decode(imageData)

        # Save the image data to a file
        with open("./image.jpg", "wb") as f:
            f.write(imageBytes)

        # Respond with a success message or the captured image URL
        print("Image captured successfully!")
    except Exception as e:
        print(f"Error saving image: {str(e)}")
else:
    print("Error: No image data received")

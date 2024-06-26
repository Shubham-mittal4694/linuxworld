import numpy as np
import matplotlib.pyplot as plt

width = 800
height = 600
channels = 3  # RGB channels

image = np.random.rand(height, width, channels)


# Display the image (optional)
plt.imshow(image)
plt.axis('off')  # Hide axes for display purposes
plt.title('Random Image')
plt.show()

# Save the image
output_filename = '/custom_image/custom_image.png'
plt.imsave(output_filename, image)

print(f"Image saved as {output_filename}")

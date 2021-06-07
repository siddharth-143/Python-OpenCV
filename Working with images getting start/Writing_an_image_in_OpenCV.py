# Python program to explain cv2.imwrite() method

# importing cv2
import cv2

# importing os module
import os

# Image path
image_path = r"../images/1.jpeg"

# Image directory
directory = r"..\images"

# Using cv2.imread() method
# to read the image
img = cv2.imread(image_path)

# Change the current directory
# to specified directory
os.chdir(directory)

# List files and directories
print("Before saving image:")
print(os.listdir(directory))

# Filename (name of image and format)
filename = 'savedImage.png'

# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, img)

# List files and directories
print("After saving image:")
print(os.listdir(directory))

print('Successfully saved')

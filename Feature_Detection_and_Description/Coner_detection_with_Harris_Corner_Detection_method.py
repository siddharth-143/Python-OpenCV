"""
    Harris Corner detection algorithm was developed to identify the internal corners
    of an image. The corners of an image are basically identified as the regions in
    which there are variations in large intensity of the gradient in all possible
    dimensions and directions. Corners extracted can be a part of the image features,
    which can be matched with features of other images,and can be used to extract
    accurate information. harris Corner Detection is a method to extract the corners
    from the input image and to extract features from the input image.
"""

# Python program to illustrate
# corner detection with
# Harris Corner Detection Method

# organizing imports
import cv2
import numpy as np

# path to input image specified and
# image is loaded with imread command
img = cv2.imread('../images/sample.jpg')

# convert the input image into
# grayscale color space
operatedImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# modify the data type
# setting to 32-bit floating point
operatedImage = np.float32(operatedImage)

# apply the cv2.cornerHarris method
# to detect the corners with appropriate
# values as input parameters
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)

# Results are marked through the dilated corners
dest = cv2.dilate(dest, None)

# Reverting back to the original image,
# with optimal threshold value
img[dest > 0.01 * dest.max()]=[0, 0, 255]

# the window showing output image with corners
cv2.imshow('Image with Borders', img)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()



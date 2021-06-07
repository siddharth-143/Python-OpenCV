"""
    Foreground Extraction in an image using Grabcut Algorithms
"""

# Python program to illustrate
# foreground extraction using
# Graabcut Algorithm

# organize import
import cv2
import numpy as np
from matplotlib import pyplot as plt

# path to input image specified and
# image is loaded with imread command
img = cv2.imread("../images/1.jpeg")

# create to simple mask image similar
# to the loaded image, with the
# shape and return type
mask = np.zeros(img.shape[:2], np.uint8)

# specify the background and foreground model
# using numpy the array is constructed of 1 row
# and 65 columns, and all array elements are 0
# data type for the array is np.float64 (default)
background_model = np.zeros((1, 65), np.float64)
foreground_model = np.zeros((1, 65), np.float64)

# define the region of Interest (RIO)
# as the coordinates of the rectangle
# where the values are entered as
# (startingPoint_x, startingPoint_y, width, height)
# these coordinates are according to the input image
# it may vary for different image
rectangle = (600, 800, 300, 350)

# apply the grabcut algorithm with appropriate
# values as parameters, number of iterations = 3
# cv2.GC_INIT_WITH_RECT is used because
# of the rectangle mode is used
cv2.grabCut(img, mask, rectangle, background_model, foreground_model, 3, cv2.GC_INIT_WITH_RECT)

# in the new mask image, pixels will
# be marked with four flags
# four flags denote the background / foreground
# mask is changed, all the 0 and 2 pixels
# are converted to the background
# mask is changed, all the 1 and 3 pixels
# are now the part of the foreground
# the return type is also mentioned,
# this gives us the final mask
mask1 = np.where((mask == 2) | (mask == 0), 0, 10).astype("uint8")

# the final mask is multiplied with
# the input to given the segmented image
img = img * mask1[:, :, np.newaxis]

# output segment image with colorbar
plt.imshow(img)
plt.colorbar()
plt.show()

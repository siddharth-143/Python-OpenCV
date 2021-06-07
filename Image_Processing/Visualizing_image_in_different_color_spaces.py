"""
    Visualizing image in different color spaces
"""

# Python program to read image as RGB

# importing cv2 and matplotlib module
import cv2
from matplotlib import pyplot as plt

# read image as RGB
img = cv2.imread("../images/logo1.png")

# read image as gray scale
# img = cv2.imread("../images/logo1.png", 0)

# we can alternatively convert image by using cv2color
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert to YCrCb color space
# img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# convert to HSV color space
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# convert to YCrCb color space
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# read image as Edge Map
# img = cv2.Laplacian(img, cv2.CV_64F)

# Heat map of image
# plt.imshow(img, cmap="hot")

# spectral image map
# plt.imshow(img, cmap="nipy_spectral")

# shows the image
plt.imshow(img, cmap="nipy_spectral")

plt.show()






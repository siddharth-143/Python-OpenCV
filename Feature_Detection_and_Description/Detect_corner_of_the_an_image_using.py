"""
    Detect corner of an image

    cv2.goodFeatureToTrack() method finds N strongest corners in the image by
    Shi-Tomasi method. Note that the image should be a grayscale image. Specify the
    number of corners you want to find and the quality level (which is a value
    between 0-1). It denotes the minimum quality of corner below which everyone is
    rejected. Then provide the minimum Euclidean distance between corners
    detected.
"""

# import the required library
import numpy as np
import cv2
from matplotlib import pyplot as plt


# read the image
img = cv2.imread('../images/logo1.png')

# convert image to gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect corners with the goodFeaturesToTrack function.
corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)
corners = np.int0(corners)

# we iterate through each corner,
# making a circle at each point that we think is a corner.
for i in corners:
	x, y = i.ravel()
	cv2.circle(img, (x, y), 3, 255, -1)

plt.imshow(img), plt.show()

"""
    Image segmentation using morphological operation in python

    If we want to extract or define something from the rest of the image, eg.
    detecting an object from a background, we can break the image up into segments
    in which we can do more processing on. This is typically called Segmentation.

    Morphological operations are some simple operations based on the image shape.
    It is normally performed on the binary images.
"""

# Python program to transform an image using threshold
import cv2
import numpy as np
from matplotlib import pyplot as plt

# image operation using thresholding
img = cv2.imread("../images/coin.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# noise removal using morphological closing operation
kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

# background area using dilation
bg = cv2.dilate(closing, kernel, iterations=1)

# finding foreground area
dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 0)
ret, fg = cv2.threshold(dist_transform, 0.02 * dist_transform.max(), 255, 0)

# display image
cv2.imshow("Image", thresh)
cv2.imshow("Image1", fg)

cv2.waitKey(0)
cv2.destroyAllWindows()
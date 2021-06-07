"""
    Edge detection in an image :

    The process of image detection involves detecting sharp edges in the image.
    This edge detection is essential in context of the image recognition or
    object localization / detection. There are several algorithms for detecting edges due
    to it's wide applicability. We'll be using one such algorithm known as Canny Edge
    Detection.
"""
import cv2
import numpy as np

path = r"../images/1.jpeg"

try:
    # read image
    img = cv2.imread(path)

    # Canny edge detection
    edges = cv2.Canny(img, 100, -200)

    # write image back to disk
    cv2.imwrite("result3.jpeg", edges)

except IOError:
    print("Error while reading files !!!")
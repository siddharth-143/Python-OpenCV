"""
    Rotating an image :

    Images can be rotated to any degree clockwise or anticlockwise. We just to
    define rotation matrix listing rotation point, degree of rotation and the scaling
    factor.
"""

import cv2
import numpy as np

path = r"../images/1.jpeg"
try:
    # read image from disk
    img = cv2.imread(path)

    # shape of image in terms of pixels
    (rows, cols) = img.shape[:2]

    # getRotationMatrix2D creates a matrix needed for transformation
    # we want matrix fir rotation w.r.t center to 45 degree without scaling
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    res = cv2.warpAffine(img, M, (cols, rows))

    # write image back to disk
    cv2.imwrite("result1.jpeg", res)

except IOError:
    print("Error while reading files !!!")
"""
    Translating an image :

    Translating an image means shifting it within a given frame of reference.
"""

import cv2
import numpy as np

path = r"../images/1.jpeg"
# create translation matrix
# if the shift is (x, y) then matrix would be
# m = [1 0 X]
#       [0 1 Y]
# let's shift by (100, 50)

M = np.float32([[1, 0, 100], [0, 1, 50]])

try:
    # read image from disk
    img = cv2.imread(path)
    (rows, cols) = img.shape[:2]

    # warpAffine does appropriate shifting given the
    # translation matrix
    res = cv2.warpAffine(img, M, (cols, rows))

    # write image back to disk
    cv2.imwrite("result2.jpeg", res)

except IOError:
    print("Error while reading files !!!")
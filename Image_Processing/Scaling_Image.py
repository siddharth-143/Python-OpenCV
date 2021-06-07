"""
    Scaling an image :

    Scaling operation increases/reduces size of an image.
"""

import cv2
import numpy as np

path = r"../images/1.jpeg"
try :
    # read image from disk
    img = cv2.imread(path)

    # get number of pixel horizontally and vertically
    (height, width) = img.shape[:2]

    # specify the size of the image along with interpolation methods
    # cv2.INTER_AREA is used for shrinking, where cv2.INTER_CUBIC
    # is used for zooming
    res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)

    # write image back to disk
    cv2.imwrite("result.jpeg", res)

except IOError:
    print("Error while reading file !!!")
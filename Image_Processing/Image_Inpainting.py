"""
    Image Inpainting

    Image Inpainting is the process of removing damage, such as noise, strokes or
    text, on images. It is particularly useful in the restoration of old photographs
    which might have scratched edges or ink spots on them. These can be digitally
    removed through this method.

    Image inpainting works by replacing the damaged pixels with pixels similar to the
    neighboring ones, therefore, making them inconspicuous and helping them
    blend well with the background.
"""

import cv2
import numpy as np

img = cv2.imread("../images/1.jpeg")

mask = cv2.imread("../images/star.jpg", 0)

dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)
cv2.imshow("image", dst)
cv2.waitKey(0)
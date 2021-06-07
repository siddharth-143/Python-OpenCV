"""
    Piecewise-Linear Transformation Function

    These functions, as the name suggests, are not entirely linear in the nature.
    However, they are linear between certain x-intervals. One of the most commonly
    used piecewise-linear transformation functions is contrast stretching.
"""

import cv2
import numpy as np

# function to map each intensity level to input intensity level
def pixel_val(pix, r1, s1, r2, s2):

    if 0 <= pix and pix <= r2:
        return (s1 / r1) * pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2) / (255 - r2)) * (pix - r2) + s2


# open the image
img = cv2.imread("../images/sample.jpg")

# define parameters
r1 = 70
s1 = 0
r2 = 140
s2 = 255

# vectorize the function to apply it to each in the numpy array
pixel_val_vec = np.vectorize(pixel_val)

# apply contrast stretching
contrast_stretched = pixel_val_vec(img, r1, s1, r2, s2)

cv2.imshow("image", contrast_stretched)

cv2.waitKey(0)
cv2.destroyAllWindows()
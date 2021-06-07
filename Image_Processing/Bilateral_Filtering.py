"""
    Bilateral Filtering

    A bilateral filter is used for smoothening images and reducing noise, while
    preserving edges.
"""

import cv2

# read the image
import numpy as np

img = cv2.imread("../images/taj.jpg")

# apply bilateral filter width s = 15
# sigmaColor = sigmaSpace = 75
bilateral = cv2.bilateralFilter(img, 15, 75, 75)

# average filter
average_filter = cv2.blur(img, (5, 5))

# median filter
median_filter = cv2.medianBlur(img, 5)

# gaussian filter
gaussian_filter = cv2.GaussianBlur(img, (5, 5), 0)

# stacking the image side-by-side
res = np.hstack((img, bilateral, average_filter, median_filter, gaussian_filter))

cv2.imshow("image", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
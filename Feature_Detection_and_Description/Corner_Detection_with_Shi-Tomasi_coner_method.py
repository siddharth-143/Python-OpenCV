"""
    Corner Detection with Shi-Tomasi Coner Detection method
"""

# Python progran to illustrate
# corner detection with
# Shi-Tomasi detection  method

# organizing imports
import cv2
import numpy as np
import matplotlib.pyplot as plt

# path to input image specified and
# image is loaded with imread command
img = cv2.imread("../images/1.jpeg")

# convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Shi-Tomasi corner detection function
# we are detecting only 100 best corner here
# you can change the number to get desired result
corner = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# convert corner value to integer
# so that we will be able to draw circles on them
corner = np.int0(corner)

# draw red color circles on all corners
for i in corner:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

# resulting image
plt.imshow(img)
plt.show()

# de-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
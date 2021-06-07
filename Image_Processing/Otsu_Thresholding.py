"""
    Python | Thresholding techniques using OpenCV
    Set-3 (Otsu Thresholding)

    In Otsu Thresholding, a value of the threshold isn't chosen but is determined
    automatically. A bimodal image (two distinct image values) is considered. The
    histogram generated contains two peaks. So, a generic condition would be to
    choose a threshold value that lies in the middle of the histogram peak
    values.
"""

# Python program to illustrate
# Otsu thresholding type on an image

# organizing import
import cv2
import numpy as np

# path to input image is specified and
# image is loaded with imread command
img = cv2.imread("../images/1.jpeg", 0)

# OR

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# applied Otsu thresholding
# as an extra flag in binary thresholding
res, thresh1 = cv2.cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# stacking image side-by-side
stack = np.hstack((img, thresh1))

# the window showing output image
# with the corresponding thresholding
# technique applied to the input image
cv2.imshow("Otsu Thresholding", stack)

# de-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

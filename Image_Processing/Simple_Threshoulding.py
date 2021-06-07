"""
    Thresholding techniques using OpenCV | Set-1 (Simple Thresholding)

    Thresholding is a technique in OpenCV, which is the assignment of pixel values in
    relation to the threshold value provided. In thresholding, each pixel value is
    compared with the thresholding value. If the pixel value is smaller than the
    thresholding, it is set to 0, otherwise, it is set to an maximum value (generally 255).
    Thresholding is very popular segmentation technique, used for separating an
    object considered as foreground from its background. A threshold is value
    which has two regions on its either side i.e below the threshold or above the
    threshold.

    In computer vision, this technique of thresholding is done on grayscale images.
    So, initially, the image has to be converted in grayscale color space.

    If f (x, y) > T
        then f (x, y) = 0
    else
        f (x, y) = 255

    where
    f (x, y) = Coordinate pixel value
    T = Threshold Value.

    Simple Thresholding :

    The basic thresholding technique is Binary Thresholding. For every pixel, the
    same threshold value is applied. If the pixel value is smaller than threshold, it
    ia set to 0, otherwise, it is set to a maximum value.

    The different Simple Thresholding Techniques are :

    cv2.THRESH_BINARY : If pixel intensity is greater than the set threshold, value set
    tp 255, else set to 0 (black)

    cv2.THRESH_BINARY_INV : Inverted or opposite case of cv2.THRESH_BINARY.

    cv2.THRESH_TRUNC : If pixel intensity value is greater than, threshold, it is
    truncated to the threshold. The pixel values are set to the same as the
    threshold. All other values remain the same.

    cv2.THRESH_TOZERO : Pixel intensity is set to 0, for all the pixel intensity, less
    than the threshold value.

    cv2.THRESH_TOZERO_INV : Inverted or opposite case of cv2.THRESH_TOZERO.
"""

# Python program to illustrate
# simple thresholding type on an image

# organizing imports
import cv2
import numpy as np

# path to input image is specified and
# image is loaded with imread command
img = cv2.imread("../images/1.jpeg")  # second parameter 0 to grayscale color

# OR

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# applying different thresholding
# techniques in the input image
# all pixels value above 120 will
# be set to 255

ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# The window showing output images
# with the corresponding thresholding
# techniques applied to the input images
cv2.imshow("Binary, Threshold", thresh1)
cv2.imshow("Binary Threshold Inverted", thresh2)
cv2.imshow("Truncate Threshold", thresh3)
cv2.imshow("Set to 0", thresh4)
cv2.imshow("Set to 0 Inverted", thresh5)

# de-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

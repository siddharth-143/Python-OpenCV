"""
    Image Blurring refers to making the image less clear or distinct. It is done with
    the help of various low pass filter kernels.

    Important types of blurring:
        Gaussian Blurring : Gaussian blur is the result of blurring an image by a
        gaussian function. It is a widely used effect in graphics software, typically to
        reduce image and reduce details. It is also used as a preprocessing stage

    Median Blur :
        The median filter is a non-linear digital filtering technique,
        often used to remove noise from an image or signal. Median filtering is very
        widely used in digital image processing because, under certain conditions, it
        preserves edges while removing noise. It is one of the best algorithms to
        remove salt and pepper noise.

    Bilateral Blur :
        A bilateral filter is a non-linear, edge-preserving, and noise-reducing
        smoothing filter for images. It replaces the intensity of each pixel
        with a weighted average of intensity values from nearby pixels. This weight
        can be based on a Gaussian distribution. Thus, sharp edges are preserved
        while discarding the weak ones.
"""

# importing libraries
import cv2
import numpy as np

img = cv2.imread("../images/1.jpeg")

cv2.imshow("Original Image", img)
# cv2.waitKey(0)

# Gaussian Blur
gaussian = cv2.GaussianBlur(img, (9, 7), 0)
cv2.imshow("Gaussian Image", gaussian)
# cv2.waitKey(0)

# Median Blur
median = cv2.medianBlur(img, 7)
cv2.imshow("Median Blur", median)
# cv2.waitKey(0)

# Bilateral blur
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow("Bilateral Blur", bilateral)
cv2.waitKey(0)

# cv2.destroyAllWindows()
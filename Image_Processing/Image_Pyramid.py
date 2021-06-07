"""
    Image Pyramid

    Image Pyramid are one of the most beautiful concept of image
    processing. Normally, we work with images with default resolution but many
    times we need to change the resolution (lower it) or resize the originally image in
    that case image pyramids come handy.

    The pyrUp() function increases the size to double of its original size and
    pyrDown() function decreases the size to half. If we keep the original image as a
    base image and go on applying pyrDown function on it and keep the images in a
    vertical stack, it will look like a pyramid. The same is true for upscaling the
    original image by ptrUp function.
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("../images/1.jpeg")

layer = img.copy()

for i in range(4):
    plt.subplot(2, 2, i + 1)

    # using pyrDown() function
    layer = cv2.pyrDown(layer)

    plt.imshow(layer)
    cv2.imshow("Image", layer)
    cv2.waitKey(0)

cv2.destroyAllWindows()
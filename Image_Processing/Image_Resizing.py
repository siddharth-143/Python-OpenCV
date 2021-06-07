"""
    Image Resizing :

    Image resizing refers to the scaling of images. Scaling comes in handy in many
    image processing as well as machine learning applications. It helps in reducing
    the number of pixels from an image and that has several advantages e.g It can
    reduce the time of training of a neural network as more is the number of pixels in
    an image more is the number of input nodes that in turn increases the complexity
    of the model.
    It also helps in zooming in image. Many times we need to resize the image i.e.
    either shrink or scale up to meet the size requirements. OpenCV provides us
    several interpolation method for resizing an image.

    Choice of Interpolation Method for Resizing :

    1. cv2.INTER_AREA : This is used when we need to shrink an image.
    2. cv2.INTER_CUBIC : This is slow but more efficient.
    3. cv2o.INTER_LINEAR : This is primarily used when zooming is required. This is
    the default interpolation technique in opencv.

    Note : One thing to keep in the mind while using the cv2.resize() function is that the
    tuple passed for determining the size of the new image ((1050, 1610) in this
    case) follows the order (width, height) unlike as expected (height, width).
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../images/star.jpg", 1)
half = cv2.resize(img, (0,0), fx=0.1, fy=0.1)
bigger = cv2.resize(img, (1050, 1610))

stretch_near = cv2.resize(img, (780, 540), interpolation=cv2.INTER_NEAREST)

title = ["Original", "Half", "Bigger", "Interpolation Nearest"]
imgs = [img, half, bigger, stretch_near]
count = 4

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(title[i])
    plt.imshow(img[i])

plt.show()
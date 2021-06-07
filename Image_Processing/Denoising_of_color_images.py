"""
    Denoising of colored images

    Denoising of an image refers to the process of reconstruction of a signal from
    noisy images. Denoising is done to remove unwanted noise from image to
    analyze it in better form. It refers to one of the major pre-processing steps.
"""

# importing libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# read image
img = cv2.imread("../images/taj.jpg")

# denoising of image saving it into dst image
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)

# ploting of source and destination image
plt.subplots(121)
plt.imshow(img)

plt.subplots(122)
plt.imshow(dst)

plt.show()
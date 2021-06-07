"""
    Python program to analyze an image using Histogram
"""

# importing required libraries of opencv
import cv2

# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread("../images/1.jpeg", 0)
img1 = cv2.imread("../images/2.jpeg")
img2 = cv2.imread("../images/3.jpeg")
img3 = cv2.imread("../images/1bit.png")

# find frequency of pixels in range 0-255
histr = cv2.calcHist([img], [0], None, [256], [0, 256])
# histr1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
# histr2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
# histr3 = cv2.calcHist([img3], [0], None, [256], [0, 256])

# show the plotting graph of an image
plt.plot(histr)
# plt.plot(histr1)
# plt.plot(histr2)
# plt.plot(histr3)

# alternative way to find histogram of an image
plt.hist(img.ravel(), 256, [0, 256])

plt.show()
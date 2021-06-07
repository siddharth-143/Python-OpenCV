"""
    cv2.cvtCOLOR() method :

    cv2.cvtCOLOR() method is used to convert an image from one color
    space to another. There are more than 15 color-space conversion methods
    available on opencv. We will use some of the color space conversion code below.
"""

# Python program to explain cv2.cvtCOLOR() method

# importing module
import cv2
import numpy as np

path = r"../images/1.jpeg"

# reading an image in default mode
img = cv2.imread(path)

# using cv2.cvtCOLOR() method
# using cv2.COLOR_BGR2GRAY color space
# conversion code
cvt = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cvt1 = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
cvt2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# display the image
cv2.imshow("image1", cvt)
cv2.imshow("image2", cvt1)
cv2.imshow("image3", cvt2)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
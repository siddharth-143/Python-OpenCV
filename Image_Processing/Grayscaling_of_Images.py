"""
    Grayscaling of Images :
        Grayscaling is the process of converting sn image from other color spaces e.g
        RGB, CMYK, HSV, etc. to shade og gray. It varies between complete black and
        complete white.
"""

# importing opencv
import cv2

# load image
img = cv2.imread("../images/1.jpeg")
cv2.imshow("original", img)

# we can cvtColor, to convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayscale", gray_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
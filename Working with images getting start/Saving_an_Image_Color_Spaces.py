"""
    Color Space in OpenCV
"""

import cv2

img = cv2.imread("../images/RGB.png")

# corresponding channels are separated
R, G, B = cv2.split(img)

cv2.imshow("original", img)
cv2.waitKey(0)

cv2.imshow("red", R)
cv2.waitKey(0)

cv2.imshow("green", G)
cv2.waitKey(0)

cv2.imshow("blue", B)
cv2.waitKey(0)


cv2.destroyAllWindows()
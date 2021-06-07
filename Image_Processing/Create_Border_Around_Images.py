"""
    cv2.copyMakeBorder() method :
        is used to create a border around the image like a photo frame.
"""

# Python program to explain cv2.copyMakeBorder() method

# importing cv2
import cv2

# path
path = r"../images/2.jpeg"

# reading an image in default mode
img = cv2.imread(path)

# window name in which image is diaplayed
win_name = "Border Image"

# using cv2.copyMakeBorder() method
img1 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(24, 41, 90))

img2 = cv2.copyMakeBorder(img, 100, 100, 50, 50, cv2.BORDER_REFLECT)

# display the image
cv2.imshow(win_name, img1)

cv2.imshow("BORDER_REFLECT", img2)

cv2.waitKey(0)

cv2.destroyAllWindows()
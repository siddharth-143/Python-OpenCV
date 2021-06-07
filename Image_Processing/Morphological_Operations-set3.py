"""
    Morphological operation is elaborated that is Gradient. It is used for generating
    the outline of the image. There are two types of gradients, internal and external
    gradient. The internal gradient enhances the internal boundaries of the objects brighter than
    their background and external gradient boundaries of objects darker than their
    background. For binary images, the internal gradient generates a mask of the internal
    boundaries of the background image object.
"""

# Python program to illustrate
# Gradient morphological operation
# on the frames

# organizing import
import cv2
import numpy as np

# return video from the first webcam on your computer
cap = cv2.VideoCapture(0)

# loop runs if capturing has been initialized
while 1:

    # reads frame from a camera
    _, img = cap.read()

    # convert to HSV color space, OCV reads color as BGR
    # frame is converted to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # defining the range of masking
    blue1 = np.array([110, 50, 50])
    blue2 = np.array([130, 255, 255])

    # initializing the mask to be
    # convoluted over input image
    mask = cv2.inRange(hsv, blue1, blue2)

    # passing the bitwise_and over
    # each pixel convoluted
    res = cv2.bitwise_and(img, img, mask=mask)

    # defining the kernel i.e structuring element
    kernel = np.ones((5, 5), np.uint8)

    # defining the gradient function
    # is show in the window
    gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

    # the mask and closing operation
    # is show in the window
    cv2.imshow("Gradient", gradient)

    # with for 'q' key associated memory usage
    if cv2.waitKey(0) & 0xff == ord('q'):
        break

# de-allocate any associated memory usage
cv2.destroyAllWindows()

# close the window / release webcam
cap.release()
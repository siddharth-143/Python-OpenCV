"""
    Filter color

    Color segmentation or color filtering is widely used in OpenCV for identifying
    specific object/regions having a specific color. The most widely used color
    space is RGB color space, it is called an additive color space as the three color
    shades add up to give color to the image. To identify a region of a specific color,
    put the threshold and create a mask to separate the different colors. HSV color
    space is much more useful fi=or this purpose as the colors in HSV space are much
    more localized thus can be easily separated. Color Filtering has many
    applications and uses cases such as Cryptography, infrared analysis, food
    preservation of perishable foods, etc. In such cases, the concepts of image
    processing can be used to find out or extract out region of a particular color.
    For color segmentation, all we need is the threshold values or the knowledge of
    the lower bound and upper bound range of color in one of the color space. It
    works best in the Hue-Saturation-Value color space.
    After specifying the range of color to be segmented, it is needed to create a mask
    accordingly and by using it, a particular region of interest can be separated out.
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    # it convert the BGR color space of image to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # threshold of blur in shv space
    lower_blue = np.array([60, 35, 140])
    upper_blue = np.array([180, 255, 255])

    # preparing the mask to overlay
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # the black region in the mask has the value of 6
    # so when multiplied with original image removes all ni=on-blue regions
    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    cv2.waitKey(0)

cv2.destroyAllWindows()
cap.release()



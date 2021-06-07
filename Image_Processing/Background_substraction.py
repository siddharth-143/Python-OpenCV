"""
    Background subtraction

    Background subtraction has several use cases in everyday life, it is being used
    for object segmentation, security enhancement, pedestrian tracking, counting
    the number of visitors, number of vehicles in traffic etc. It is able to learn and
    identify the foreground mask.

    As the name suggests, it is able to subtract or eliminate the background portion
    in an image. Its output is a binary segmented image which essentially gives
    information about the non-stationary objects in the image. There lies a problem
    in this concept of finding non-stationary portion, as the shadow of the moving
    object can be moving and somethings being classified in the foreground.

    The popular Background subtraction algorithms are :

    BackgroundSubtractionMOG : It is a gaussian mixture based background
    segmentation algorithm.

    BackgroundSubtractionMOG : It uses the same concept but the major advantage
    that it provides is in terms if stability even when there is change in luminosity
    and better identification capability of shadows in the frames.

    Geometric multigrid : It makes uses of statistical method and per pixel
    bayesin segmentation algorithm.
"""

# Python program for background subtraction
import cv2
import numpy as np

cap = cv2.VideoCapture("../Videos/v.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()

while 1 :
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow("fgmask", fgmask)
    cv2.imshow("frame", frame)

    k = cv2.waitKey(0) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
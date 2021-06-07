"""
    Circle Detection

    Circle detection finds a variety of uses in biomedical application, ranging from
    iris detection to white blood cell segmentation. The technique followed is similar
    to the one used to detect line.
"""

import cv2
import numpy as np

# read image
img = cv2.imread("../images/s2.jpg", cv2.IMREAD_COLOR)

# convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur using 3 * 3 kernel
gray_blurred = cv2.blur(gray, (3, 3))

# apply Hough transform on the blurred image
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=1, maxRadius=40)

# draw circle that are detected
if detected_circles is not None:

    # convert the circle parameters a, b and r to integers
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # draw the circumference of the circle
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        # draw a small circle (of radius 1) to show the center
        cv2.circle(img, (a, b), r, (0, 255, 0), 3)
        cv2.imshow("Detected circle", img)
        cv2.waitKey(0)

cv2.destroyAllWindows()
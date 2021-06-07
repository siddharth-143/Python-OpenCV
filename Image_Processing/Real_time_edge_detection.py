"""
    Real time edge detection
"""

# import libraries of OpenCV
import cv2

# import numpy by alias np
import numpy as np

# capture frame from a camera
cap = cv2.VideoCapture(0)

# loop runs if capturing has been initialized
while (1):

    # reads frames from camera
    ret, frame = cap.read()

    # converting BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])

    # create a red HSV color boundary and
    # threshold HSV image
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # display an original image
    cv2.imshow("Original image", frame)

    # discovers edge in the input image and
    # marks them in the output map edges
    edges = cv2.Canny(frame, 100, 200)

    # display edge in a frame
    cv2.imshow("Edges", edges)

    # wait for Esc key to stop
    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break

# close the window
cap.release()

# de-allocate any associated memory usage
cv2.destroyAllWindows()

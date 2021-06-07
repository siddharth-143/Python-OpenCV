"""
    Opening multiple color windows to capture image
"""

# importing the required modules
import cv2
import numpy as np

# capturing from the first camera attached
cap = cv2.VideoCapture(0)

# will continue to capture until 'q' key is pressed
while True:

    ret, frame = cap.read()

    # capturing in grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame", frame)
    cv2.imshow("gray", gray)

    # program will terminate when 'q' key is pressed
    if cv2.waitKey(0) & 0xff == ord('q'):
        break

# releasing all the resources
cap.release()
cv2.destroyAllWindows()
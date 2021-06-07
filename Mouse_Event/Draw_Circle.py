"""
    Mouse Event

    Mouse as a paint brush

    OpenCV provides a facility to use the mouse as a paint brush or a drawing tool.
    Whenever any mouse event occurs on the window screen, it can draw anything.
    Mouse events can be left-button up, double-click, etc. It gives us the
    coordinates (x, y) for every mouse event. By using these coordinates, we can draw
    whatever we want. To get the list of all available events, run the following code in
"""

import cv2
import numpy as np


# Creating mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # create a circle
        cv2.circle(img, (x, y), 100, (255, 255, 0), -1)


# Creating a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)

# window name
cv2.namedWindow('image')

# set mouse event
cv2.setMouseCallback('image', draw_circle)

while (1):

    # display window
    cv2.imshow('image', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()

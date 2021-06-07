"""
    OpenCV Canny Edge Detection :

    Edge detection is term where identify the boundary of object in image.
"""

# importing module
import cv2
import numpy as np

# image path
img = cv2.imread("../images/1.jpeg")
# canny edge detection
edges = cv2.Canny(img, 100, 200)

# display the image
cv2.imshow("Edge detection image", edges)
cv2.imshow("Original image", img)

# waits until a key is pressed
cv2.waitKey(0)

# destroys the window showing image
cv2.destroyAllWindows()

"""
    Python OpenCV | cv2.imshow() method

    cv2.imshow() method is used to display an image in a window.
    The window automatically fits to the image size.
"""

# Python program to explain cv2.imshow() method

# importing cv2
import cv2

# path
path = r"../images\1.jpeg"

# Reading an image in default mode
image = cv2.imread(path)

# window name in which image is displayed
win_name = "opencv"

# Using cv2.imshow() method
# Displaying the image
cv2.imshow(win_name, image)

# waits for user to press any key
# (this is necessary to avoid python kernel from crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
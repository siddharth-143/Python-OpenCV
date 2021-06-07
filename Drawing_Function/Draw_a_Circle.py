"""
    cv2.circle() method :

    cv2.circle() method is used to draw a circle on any image.
"""

# Python program to explain cv2.circle() method

# importing cv2
import cv2

# path
path = "../images/1.jpeg"
path1 = "../images/3.jpeg"

# reading an image in default is displayed
img = cv2.imread(path)
img_1 = cv2.imread(path1)

# window name in which image is displayed
win_name = "circle"

# center coordinates
center_coordinates = (203, 232)
center_coordinates1 = (291, 150)

# radius of circle
radius = 10
radius1 = 5

# blue color in BGR
color = (255, 0, 0)
color1 = (0, 255, 0)

# line thickness in px
thickness = 2
thickness1 = -1

# using cv2.circle() method
# draw a circle with blue line borders of thickness
img1 = cv2.circle(img, center_coordinates, radius, color, thickness)
img2 = cv2.circle(img_1, center_coordinates1, radius1, color1, thickness1)

# displaying the image
cv2.imshow(win_name, img1)
cv2.imshow("circle1", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
    cv2.ellipse() :

    cv2.ellipse() method is used to draw a ellipse on any image.
"""

# Python program to explain cv2.ellipse() method

# importing cv2
import cv2

# path
path = r"../images/1.jpeg"

# reading an image in default mode
img = cv2.imread(path)

# window name in which image is displayed
win_name = "Ellipse"

center_coordinates = (220, 300)

axes_length = (200, 100)

angle = 0

start_angle = 0

end_angle = 360

# color in RGB
color = (0, 0, 255)

# line thickness of 5 px
thickness = 5

# using cv2.ellipse() method
# draw a ellipse with color line borders of the thickness of 5 px
img = cv2.ellipse(img, center_coordinates, axes_length, angle, start_angle, end_angle, color, thickness)

# display the image
cv2.imshow(win_name, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
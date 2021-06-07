"""
    cv2.rectangle() :

    cv2.rectangle() method is used to draw a rectangle on any image.
"""

# Python program to explain cv2.rectangle() method.

# importing cv2
import cv2

# path
path = "../images/1.jpeg"

# reading an image in default mode
img = cv2.imread(path)

# window name in which image is displayed
win_name = "Rectangle"

# start coordinates
# represents the top left corner of rectangle
start_point = (120, 150)

# end coordinates
# represents the bottom right corner of rectangle
end_point = (300, 500)

# color in RGB
color = (255, 0, 0)

# line thickness
thickness = 2
thickness1 = -2

# using cv2.rectangle() method
# draw a rectangle with color line borders of thickness
img = cv2.rectangle(img, start_point, end_point, color, thickness)

# displaying the image
cv2.imshow(win_name, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
    cv2.line() :

    cv2.line() method is used to draw a line on any image
"""

# Python progrsm to explain cv2.line() method

# importing cv2
import cv2

# path
path = r"../images/1.jpeg"

# reading an image in default mode
img = cv2.imread(path, 0)

# windows name in which image is displayed
win_name = "Image Line"

# start coordinate, here (0, 0)
# represents the top left corner of image
start_point = (0, 0)
start_point1 = (500, 0)

# end coordinate, here (250, 250)
# represents the bottom right corner of image
end_point = (750, 1130)
end_point1 = (0, 750)

# color in BGR
color = (0, 0, 255)

# line thickness in pixels
thickness = 9

# using cv2.line() method
# draw a diagonal color line with thickness
img = cv2.line(img, start_point, end_point, color, thickness)
img = cv2.line(img, start_point1, end_point1, color, thickness)


# display the image
cv2.imshow(win_name, img)

cv2.waitKey(0)
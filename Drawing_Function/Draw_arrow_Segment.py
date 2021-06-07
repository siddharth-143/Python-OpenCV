"""
    cv2.arrowsLine() method :

    cv2.arrowedLine() method is used to draw arrow segment pointing from the start
    point to the end point.
"""

# Python program to explain in default mode

# importing cv2
import cv2

# path
path = r"../images/1.jpeg"

# reading an image in default mode
img = cv2.imread(path)

# window name in which image is displayed
win_name = "Arrow Image"

# start coordinate, here (0, 0)
# represents the top left corner of image
start_point = (0, 0)
start_point1 = (500, 0)

# end coordinates
end_point = (470, 730)
end_point1 = (30, 730)

# color in RGB
color = (0, 255, 0)

# line thickness
thickness = 5

# using cv2.arrowedLine() method
# draw a diagonal color arrow line
# with thickness
img = cv2.arrowedLine(img, start_point, end_point, color, thickness)
img = cv2.arrowedLine(img, start_point1, end_point1, color, thickness)

# display the image
cv2.imshow(win_name, img)

cv2.waitKey(0)
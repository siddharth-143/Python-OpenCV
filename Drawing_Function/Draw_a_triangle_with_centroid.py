"""
    Draw a triangle using centroid

    Approach :

    Create a black window with three color channels with resolution 400x300. Draw
    three lines which are passing through the given points using the built line
    function of the OpenCV. It will create a triangle on the black window. Find the
    centroid of the triangle using the following formula.

    (x, y) = { x1+x2+x3 / 3, y1+y2+y3 / 3}

    Draw this centroid on the window using circle function OpenCV with zero
    thickness.
"""

# Python code to draw a triangle and find centroid

# import libraries
import cv2
import numpy as np

# with and height of the window
width = 400
height = 300

# create a window of 400x300
img = np.zeros((height, width, 3), np.uint8)

# three vertices (tuple) of the triangle
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 100)

# drawing the triangle with the help of lines
# on the window with the given points
# cv2.line is the built function in opencv library
cv2.line(img, p1, p2, (255, 0, 0), 3)
cv2.line(img, p2, p3, (0, 255, 0), 3)
cv2.line(img, p1, p3, (0, 0, 255), 3)

# finding centroid using the following formula
# (x, y) = (x1 + x2 + x3 // 3, y1 + y2 + y3 // 3)
centroid = ((p1[0]+p2[0]+p3[0])//3, (p1[1]+p2[1]+p3[1])//3)

# drawing the centroid on the window
cv2.circle(img, centroid, 4, (0, 255, 0))

# image is the title on the window
cv2.imshow("images", img)
cv2.waitKey(0)
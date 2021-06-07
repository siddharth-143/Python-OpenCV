"""
    Find and Draw Contours using OpenCV

    Contours are define as the line joining all the points along the boundary of an
    image that are having the same intensity. Contours come handy in shape
    analysis, finding the size of the object of interest, and object detection.

    OpenCV findContour() method that helps in extracting the contours from the
    image. It works best on binary image, so we should first apply thresholding
    techniques, Sobel edges, etc.
"""

# importing module
import cv2
import numpy as np

# image
img = cv2.imread("../images/2bit.png", 0)

# or to change image mode to gray
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find Canny edges of object
edged = cv2.Canny(img, 30, 200)

# finding contours
# using a copy of the image e.g. edged.copy()
# since findCounters alters the image
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# stacking image step-by-step
res = np.hstack((img, edged))

cv2.imshow("Canny edges after contouring", res)

print("Number of contours found = " + str(len(contours)))

# draw all contours
# -1 signifies drawing all contours
cv2.drawContours(img, contours, -1, (0, 255, 0), -3)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()



"""
    Contours Approximation Method :
    
    Above, we see that contours are the boundaries of a shape with the same
    intensity. It stores the (x, y) coordinates of the boundaries of a shape. But does it
    store all the coordinates? That is specified by this contours approximation
    method.
    
    If we pass cv2.CHAIN_APPROX_NONE, all the boundaries points are stored. But
    actually, do we need all the points? For eg, if we have to find the contour of a 
    straight line. We need just two endpoints of that line. This is what
    cv2.CHAIN_APPROX_SIMPLE does. It removes all redundant points and compresses
    the contour, thereby saving memory.
"""
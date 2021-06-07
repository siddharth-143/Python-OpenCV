"""
    Image translation

    Translation refers to the rectilinear shit of an object i.e an image from one
    location to another. If we know the amount of shift in horizontal and the vertical
    direction, say (tx, ty) then we can make a transformation matrix e.g
    where tx denotes the shift along the x-axis and ty denotes shift along y-axis
    i.e the number of pixels by which we need to shift about in that direction.
    Now, we can use the cv2.wrapAffine() function to implement these translations.
    This function requires a 2x3 array. The numpy array should be of float type.
"""
import cv2
import numpy as np

img = cv2.imread("../images/3.jpeg")

# store height and width of the image
height, width = img.shape[:2]

quarter_height, quarter_width = height / 10, width / 10

T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])

# we use wrapAffine to transform
# the image using the matrix, T
img_translation = cv2.warpAffine(img, T, (width, height))

# stacking image side-by-side
# res = np.hstack((img, img_translation))

cv2.imshow("Original Image", img)
cv2.imshow("Translation Image", img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
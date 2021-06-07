"""
    Python | Thresholding techniques using OpenCV
    Set-2 (Adaptive Thresholding)

    Simple Thresholding was explained with different types of
    thresholding techniques. Another Thresholding techniques is Adaptive
    Thresholding. In Simple Thresholding technique, a global value of threshold was used
    which remained constant throughout. So, a constant threshold value won't help
    in the case of variable lighting conditions in different areas. Adaptive
    thresholding is the method where the threshold value is calculated for smaller
    regions. This lead to different threshold values for different region with
    respect to the changing in lighting. We use cv2.adaptiveThreshold for this.
"""

# Python program to illustrate
# adaptive thresholding type on an image

# organizing imports
import cv2
import numpy as np

# path to input image is specfied and
# image is loaded with imread command
img = cv2.imread("../images/1.jpeg", 0)

# OR

# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# applying different thresholding
thresh1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)

thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)

# stacking image side-by-side
res = np.hstack((img, thresh1, thresh2))

# the window showing output images
# with the corresponding thresholding
# techniques applied to the input image

cv2.imshow("Adaptive Thresholding", res)
# cv2.imshow("Adaptive Gaussian", thresh2)

# de-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
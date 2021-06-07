"""
    Find circles and ellipses in an image

    To identify circles, ellipses or in general any shape in which the pixels are
    connected we use the SimpleBlobDetector() function of OpenCv. In non-technical
    terms, a blob is understood as a thick liquid drop. Here, we are going to call all
    shapes as a blob. Our task is to detect and recognize whether the blob is a circle
    or not.
"""

import cv2
import numpy as np

# load image
img = cv2.imread("../images/RGB.png", 0)

# set our filtering parameters
# initialize parameters settimg using cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# set area filtering parameters
params.filterByArea = True
params.minArea = 100

# se circularity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.2

# set incertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.01

# create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)

# detect blob
keypoints = detector.detect(img)

# draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(img, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
text = "Number of circular blobs : "+ str(len(keypoints))
cv2.putText(blobs, text, (20, 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)

# show blobs
cv2.imshow("Filtering circular blobs only", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
Reading an image in opencv using python
    To read the images cv2.imread() method is used. This method loads an image
    from the specified file.
    Note : The method should be in the working directory or a full path of image
    should be given.
"""

import cv2

# To read image from disk
path = r"../images/1.jpeg"

# img = cv2.imread(path, cv2.IMREAD_COLOR)
# or
# img = cv2.imread(path, 1)

# Using 0 to read image in grayscale mode
# img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# or
# img = cv2.imread(path, 0)

# Using 0 to read image in LOAD mode
# img = cv2.imread(path, cv2. IMREAD_LOAD_GDAL)
# OR
img = cv2.imread(path, -1)

# Create GUI window to display an image on screen
cv2.imshow("image", img)

# To hold the window on screen, we use cv2.waithKey method
cv2.waitKey(0)

# It is for removing/deleting created GUI window from screen
cv2.destroyAllWindows()
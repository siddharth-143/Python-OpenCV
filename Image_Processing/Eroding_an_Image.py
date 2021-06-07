"""
    cv2.erode() method :

    cv2.erode() method is used to perform erosion on the image. The
    basic idea of erosion is just like soil erosion only, it erodes away the boundaries
    of foreground object (Always try to keep foreground in white). It is normally
    performed on binary images. It needs two inputs, one is our original image,
    second one is called structuring element or kernel which decides the nature of
    operation. A PIXEL IN THE ORIGINAL IMAGE (EITHER 1 OR 0) WILL BE considered 1 only if
    all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
"""

# Python program to explain cv2.erode() method

# importing cv2
import cv2

# importing numpy
import numpy as np

# path
path = r'../images/3.jpeg'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Creating kernel
kernel = np.ones((6, 6), np.uint8)

# Using cv2.erode() method
image1 = cv2.erode(image, kernel, cv2.BORDER_WRAP)

# stacking image side-by-side
res = np.hstack((image, image1))

# Displaying the image
cv2.imshow(window_name, res)

# de-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

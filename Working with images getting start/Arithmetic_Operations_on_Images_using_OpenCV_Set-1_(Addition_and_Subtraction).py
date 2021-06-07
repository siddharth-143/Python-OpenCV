"""
    Arithmetic operation on image using opencv | Set-1 (addition and subtraction)

    We can add two images by using function cv2.add().
    This directly adds up image pixels in the two images.

    Syntax :
        cv2.add(img1, img2)

    But adding the pixels is not an ideal situation. So, we use cv2.addweighted().
    Remember, both images should be of equal size and depth.
"""

# Python program to illustrate
# arithmetic operation of
# addition of two images

# organizing imports
import cv2
import numpy as np

# path to input images are specified add
# images are loaded with imread command
img1 = cv2.imread("../images/1.jpeg")
img2 = cv2.imread("../images/3.jpeg")

img3 = cv2.imread("../images/star.jpg")
img4 = cv2.imread("../images/dot.jpg")

# cv2.addWeighted is applied over the
# image input with applied parameter
weighted_sum = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)

# cv2.subtract is applied over the the
# image inputs with applied parameters
sub = cv2.subtract(img3, img4)

# cv2.multiply is applied over the the
# image inputs with applied parameters
mul = cv2.multiply(img1, img2, 4000, 0.4, 0)

# cv2.divide is applied over the the
# image inputs with applied parameters
div = cv2.divide(img1, img2)

# the window showing output image
# with the weighted sum
cv2.imshow("Weighted image", weighted_sum)

# the window showing output image
# with the subtract image
cv2.imshow("Subtracted Image", sub)

# the window showing output image
# with the multiply image
cv2.imshow("Multiply Image", mul)

# the window showing output image
# with the divide image
cv2.imshow("Divide Image", div)

# de-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
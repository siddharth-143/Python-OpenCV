"""
    Arithmetic Operations on Images using OpenCV | Set-2 (Bitwise Operations on Binary Images)

    bitwise operations are used in image manipulation and used for extracting
    essential parts in the image.

    Bitwise operation used are :
        1. AND
        2. OR
        3. XOR
        4. NOT

    Also, bitwise operation helps in image masking. Image creation can be enabled
    with the help of these operations can be helpful in enhancing the properties
    of the input image.

    Note : The bitwise operations should be applied on input images of same dimensions
"""

# python programe to illustrate
# arithmetic operation of
# bitwise operation on two images
import cv2
import numpy as np

# AND : Bit-wise conjunction of input array elements.
# OR : Bit-wise disjunction of input array elements.
# XOR : Bit-wise exclusive-OR operation on input array elements.
# NOT : Inversion of input array elements.


# path to input images are specified and
# images are loaded with imread command
img1 = cv2.imread("../images/1bit.png")
img2 = cv2.imread("../images/2bit.png")


# cv2.bitwise_and is applied over the
# image input with applied parameters
dest_and = cv2.bitwise_and(img1, img2)


# cv2.bitwise_or is applied over the
# image input with applied parameters
dest_or = cv2.bitwise_or(img1, img2)

# cv2.bitwise_xor is applied over the
# image input with applied parameters
dest_xor = cv2.bitwise_xor(img1, img2)

# cv2.bitwise_not is applied over the
# image input with applied parameters
dest_not = cv2.bitwise_not(img1, img2)

# the window showing output image
# with the bitwise AND operation
# on the input images
cv2.imshow("Bitwise And", dest_and)

# the window showing output image
# with the bitwise OR operation
# on the input images
cv2.imshow("Bitwise Or", dest_or)

# the window showing output image
# with the bitwise XOR operation
# on the input images
cv2.imshow("Bitwise Xor", dest_xor)

# the window showing output image
# with the bitwise NOT operation
# on the input images
cv2.imshow("Bitwise Not", dest_not)

# de-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
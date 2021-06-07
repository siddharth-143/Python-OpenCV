"""
    We will be using find Contour() function that helps in extracting the
    contours from the image.

    Approach :

    The coordinates of each vertices of a contours is hidden in the contour itself. In
    this approach, we will be using numpy library to convert all the co-ordinates of a
    contour into a linear array. This linear array would contain the x and y
    coordinates of each contour. The key point here is that the first co-ordinate in
    the array would always be the co-ordinate of the topmost vertex and hence could
    help in detection of orientation of an image.

"""

# Python code to find the co-ordinates of
# the contours detected in an image
import cv2
import numpy as np

# font
font = cv2.FONT_HERSHEY_COMPLEX

# reading image
img2 = cv2.imread("../images/star.jpg", cv2.IMREAD_COLOR)

# reading same image in another
# variable and converting to gray scale
img = cv2.imread("../images/star.jpg", cv2.IMREAD_GRAYSCALE)

# converting image to a binary image
# black and white only image
_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

# detecting contours in image
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# going through every contours found in the image
for cnt in contours:

    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

    # draws boundary of contours
    cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)

    # used to flatter the array containing
    # the co-ordinates of the vertices
    n = approx.ravel()
    i = 0

    for j in n:
        if i % 2 == 0:
            x = n[i]
            y = n[i + 1]

            # string containing the co-ordinates
            string = str(x) + " " + str(y)

            if i == 0:
                # text on remaining the co-ordinates
                cv2.putText(img2, "Arrow tip", (x, y), font, 0.5, (255, 0, 0))
            else:
                # text on remaining co-ordinates
                cv2.putText(img2, string, (x, y), font, 0.5, (0, 255, 0))
        i += 1

# showing the final image
cv2.imshow("image", img2)

# exiting the window if 'q' is pressed on the keyboard
if cv2.waitKey(0) & 0xff == ord("q"):
    cv2.destroyAllWindows()
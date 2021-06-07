import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img = cv2.imread("../Harry_Potter/image.jpg")

while cap.isOpened():

    # take frame
    ret, frame = cap.read()

    if ret:

        # convert rgb to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])

        # add the range
        mask = cv2.inRange(hsv, l_red, u_red)

        # display background beyond the red color
        part1 = cv2.bitwise_and(img, img, mask=mask)
        # cv2.imshow("part1", part1)

        # defining the kernel i.e structuring element
        kernel = np.ones((5, 15), np.uint8)

        mask = cv2.bitwise_not(mask)

        # defining the opening function
        # over the image and structuring element
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        cv2.imshow("Opening", opening)

        # detected red color
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("clock", part1 + part2)

        if cv2.waitKey(5) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
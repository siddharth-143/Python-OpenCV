"""
    Extract image from videos

    Image Analysis is a very common field in the area of computer vision. It is the
    extraction of meaning information from videos or images. OpenCV library can
    be used to perform multiple operations on videos.
"""

# importing all necessary libraries
import cv2
import os

# read the video from specified path
cap = cv2.VideoCapture("../Videos/v.mp4")

try:

    # creating a folder named data
    if not os.path.exists("data"):
        os.makedirs("data")

# if not created then raise error
except OSError:
    print("Error : Creating directory of data")

# frame
current_frame = 0

while True:

    # read from frame
    ret, frame = cap.read()

    if ret:
        # if video is till left continue creating images
        name = "./data/frame" + str(current_frame) + ".jpg"
        print("Creating..." + name)

        # writing the extract image
        cv2.imwrite(name, frame)

        # increasing counter so that ut will
        # show how many frames are created
        current_frame += 1

    else:
        break

# release all space and windows once done
cap.release()
cv2.destroyAllWindows()



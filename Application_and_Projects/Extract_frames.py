"""
    Extract frames
"""

# Program to read video
# and extract frames
import cv2


# function to extract frames
def frame_capture(path):

    # path to video file
    cap = cv2.VideoCapture(path)

    # used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:

        # cap object calls read
        # function extract frames
        success, image = cap.read()

        # saves the frames with frame-count
        cv2.imwrite("frame%d.jpg" % count, image)

        count += 1

# driver code
if __name__ == "__main__":

    # calling the function
    frame_capture("../Videos/v.mp4")

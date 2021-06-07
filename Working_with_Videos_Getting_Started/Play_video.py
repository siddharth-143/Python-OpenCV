"""
    Play Video

    To capture a video, we need to create a VideoCapture object. VideoCapture have
    the device index or the name of a video file. Device index is just the number to
    specify which camera.If we pass 0 then it is for first camera, 1 for second camera
    so on. We capture the video frame by frame.

    Syntax :

    cv2.VideoCapture(0): Means first camera or webcam.
    cv2.VideoCapture(1): Means second camera or webcam.
    cv2.VideoCapture("file name.mp4"): Means video file
"""

# importing libraries
import cv2
import numpy as np

# video path
path = "../Videos/v.mp4"

# create a VideoCapture object and read from input file
cap = cv2.VideoCapture(path)

# check if camera opened successfully
if cap.isOpened() == False:
    print("Error opening video file")

while cap.isOpened():

    # capture frame-by-frame
    ret, frame = cap.read()

    if ret == True:

        # display the resulting frame
        cv2.imshow("Frame", frame)

        # press Q on keyboard to exit
        if cv2.waitKey(0) & 0xff == ord("q"):
            break
            # break the loop

        else:
            break

    # when everything done, release
    # the video capture object
    cap.release()

    # close all the frame
    cv2.destroyAllWindows()

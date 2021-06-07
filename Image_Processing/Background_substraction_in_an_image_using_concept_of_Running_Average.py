"""
    Background Subtraction in an image using concept of Running Average

   Background subtraction is a technique for separating out foreground elements
   from the background and is 9881721517 done generating a foreground mask. This
   technique is used for detecting dynamically moving objects from static camera.
   Background subtraction technique is important for object tracking. There are
   several techniques for background subtraction.

   The running average of a function is used to separate foreground from background.
    In this concept, the video sequence is analyzed over a particular set of frames.
    During this sequence of frames, the running average over the current frame and
    the previous frames is computed. This gives us the background model and any new
    object introduced in the during the sequencing of the video becomes the part of
    the foreground. Then, the current frame holds the newly introduced object with
    the background. Then the computation of the absolute difference between the
    background model (which is a function of time) and the current frame (which is
    newly introduced object) is done.
"""

# Python program to illustrate background subtraction using
# concept of Running Average

# organize imports
import cv2
import numpy as np

# capture frames from a camera
cap = cv2.VideoCapture(0)

# read the frame from the camera
_, img = cap.read()

# modify the data type
# setting to 64-bit floating point
average_value = np.float64(img)

# loop runs if capturing has been initialized
while 1:
    # reads frames from a camera
    _, img = cap.read()

    # using the cv2.accumulateWeighted() finction
    # thta update the running average
    cv2.accumulateWeighted(img, average_value, 0.02)

    # converting the matrix elements to absolute values
    # and converting the result to 8-bit
    result_frame = cv2.convertScaleAbs(average_value)

    # show two output windows
    # the input / original frames window
    cv2.imshow("InputWindow", img)

    # the window showing output of alpha value 0.02
    cv2.imshow("Average value", result_frame)

    # wait for esc key to stop the program
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# close the window
cap.release()

# de-allocate any associated memory usage
cv2.destroyAllWindows()
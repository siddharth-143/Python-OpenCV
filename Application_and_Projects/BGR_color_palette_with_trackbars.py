"""
    BGR  color palette with trackbars :

    Create a black window with three color channels with resolution 512x512. Then
    create three "B""G""R" trackbars using predefined functions of opencv library. Set
    the values of channels from 0 to 255. Merging the black window with these color
    trackbars.
"""

# Python program to create RGB color
# palette with trackbars

# importing libraries
import cv2
import numpy as np

# empty function called when
# any trackbar moves
def empty_function():
    pass

def main():

    # black window having 3 color channels
    img = np.zeros((512, 512, 3), np.uint8)
    window_name = "OpenCV color Palette"

    # window name
    cv2.namedWindow(window_name)

    # there trackbars which have the name
    # of trackbars min and max value
    cv2.createTrackbar("Blue", window_name, 0, 255, empty_function)
    cv2.createTrackbar("Green", window_name, 0, 255, empty_function)
    cv2.createTrackbar("Red", window_name, 0, 255, empty_function)

    # used to open the window
    # till press the ESC key
    while True:
        cv2.imshow(window_name, img)

        if cv2.waitKey(1) == 27:
            break

        # values of blue, green, red
        blue = cv2.getTrackbarPos("Blue", window_name)
        green = cv2.getTrackbarPos("Green", window_name)
        red = cv2.getTrackbarPos("Red", window_name)

        # merge all three color channels and
        # make the image composites image from rgb
        img[:] = [blue, green, red]
        print(blue, green, red)

    cv2.destroyAllWindows()

# calling main()
if __name__=="__main__":
    main()
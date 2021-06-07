"""
    cv2.putText() :

    cv2.putText() method is used to draw a text string on any image.
"""

# Python program to explain cv2.putText() method

# importing cv2
import cv2

# path
path = "../images/1.jpeg"

# reading an image in default mode
img = cv2.imread(path)

# window name in which image is displayed
win_name = "Text"

# font
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
font1 = cv2.FONT_HERSHEY_SIMPLEX

# text
text = "Hello World"
text1 = "Super....!"

# org
org = (170, 100)
org1 = (170, 600)

# fontScale
fontScale = 1
fontScale1 = 2

# color in RGB
color = (255, 0, 0)
color1 = (0, 0, 255)

# line thickness
thickness = 2
thickness1 = 5

# using cv2.putText() method
img = cv2.putText(img, text, org, font, fontScale, color, thickness, cv2.LINE_AA)

img = cv2.putText(img, text1, org1, font1, fontScale1, color1, thickness1, cv2.LINE_8, False)

img = cv2.putText(img, text1, org1, font1, fontScale1, color1, thickness1, cv2.LINE_8, True)

# displaying the image
cv2.imshow(win_name, img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
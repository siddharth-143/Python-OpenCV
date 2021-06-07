"""
    Intensity Transformation Operations on Images

    Intensity transformation are applied on images for contrast manipulation or
    image thresholding. These are in the spatial domain, i.e they are performed
    directly on the pixels of the image at hand, as opposed to being performed on the
    Fourier transform of the image.

    The following are commonly used intensity transformations :

    1. Image Negatives(Linear)
    2. Log Transformation
    3. Power-Law (Gamma) Transformations
    4. Piecewise-Linear Transformation Function

    Image Negatives :

    Mathematically, assume that an image goes from intensity level 0 to (L - 1).
    Generally, L = 256. Then, the negative transformation can be described by the
    expression s = L-1-r where r is the initial intensity level and s is the final
    intensity level and s is the final intensity level of a pixel. This produces a
    photographic negative.

    Log Transformation :

    Mathematically, log transformations can be expressed as s = clog(1+r). Here, s
    is the output intensity, r>=0 is intensity of the pixel, and c is a scaling
    constant. c is given by 255/(log (1 + m)), where m is thr maximum pixel value in
    the image. It is done to ensure that the final pixel value does not exceed (L - 1), or
    255. Practically, log transformation maps a narrow range of low-intensity input
    values to a wide range of output values.

    Power-Law (Gamma) Transformation :

    Power-law (Gamma) Transformations can be mathematically expressed as
    s = cr^{/gamma}. Gamma correction is important for displaying images in a
    screen correctly types of monitors with different display settings. This is done because
    out eyes perceive images in a gamma-shape curve, whereas cameras capture
    images in a linear fashion.
"""

import cv2
import numpy as np

# open the image
img = cv2.imread("../images/sample.jpg")

# apply log transform
c = 255/(np.log(1 + np.max(img)))
log_transformed = c * np.log(1 + img)

# specify the data type
log_transformed = np.array(log_transformed, dtype=np.uint8)

# trying 4 gamma values
for gamma in [0.1, 0.5, 1.2, 2.2, 5]:

    # apply gamma correction
    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype="uint8")
    cv2.imshow("Power-Law (Gamma) Transformation", gamma_corrected)

    cv2.waitKey(0)

# display image
cv2.imshow("Log_Transformation", log_transformed)
cv2.waitKey(0)

cv2.destroyAllWindows()
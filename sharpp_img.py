import cv2
import numpy as np

"""
Definition: Image sharpening is an image-processing technique used to enhance edges and fine details, making an image appear clearer.

"""

image = cv2.imread('blurr_img.jpg')

karnel_matrix =  np.array([[0,-1,0],
                           [-1,5,-1],
                           [0,-1,0]])

if image is None:
    print("Image not found.")

else:
    sharp_imag= cv2.filter2D(image,-1,karnel_matrix)

    cv2.imshow("sharped_img",sharp_imag)
    cv2.waitKey(0)
    cv2.destroyWindow()

"""
1. Working
1. Detect rapid changes in pixel intensity (edges).
2. Enhance those changes.
3. Add the enhanced details back to the original image.
4. Produce a sharper-looking image.

"""
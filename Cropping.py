

import cv2

img = cv2.imread("OpenCV.py/Test.jpg")
h,w,c = img.shape
# cropping in OpenCV means taking a rectangular portion of an image.
"""
Syntax:
cropped = img[y1:y2, x1:x2]
where 
[height/y, width/x] → [rows, columns]
""" 
print(f'The high is {h} and width is {w}')
Cropped = img[200:467,55:250]
cv2.imshow("OG_img", img)
cv2.imshow("Cropped_img",Cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("Cropped_the_Goku_Face.jpg",Cropped)

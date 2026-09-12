
import cv2

img = cv2.imread("OpenCV.py/Test.jpg")

'''
cv2.putText() is used in OpenCV to write/draw text directly onto an image or video frame.

'''

text = " I hear you are strong? "
origin = (70,400) 
fontsize = 0.75
color = (10,30,0)
"""
Syntax :
cv2.putText(image, text, position(bottom-left), font, font_scale, color, thickness)

"""


cv2.putText(img, text, origin, cv2.FONT_ITALIC, fontsize, color, thickness= 4 )
cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Adding_in_img.jpg", img)

import cv2
img = cv2.imread("resize_of_test.jpg")
h,w = img.shape[:2]
"""
or
h,w,c = img.shape
"""
center = (w//2,h//2)

Method_rotation = cv2.getRotationMatrix2D(center, 180, 1.25 )
Rotate_img = cv2.warpAffine(img,Method_rotation,(w,h))

cv2.imshow("180_dedree_img", Rotate_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("rotated_img", Rotate_img)
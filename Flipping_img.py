import cv2
img = cv2.imread("resize_of_test.jpg")

flip_vertical = cv2.flip(img,0) # vertical flip (top to bottom)
flip_Horizontal = cv2.flip(img,1) # horizontal flip (left to right)
flip_both = cv2.flip(img,-1) #flip from both 
cv2.imshow("og_img", img)
cv2.imshow("vertical", flip_vertical)
cv2.imshow("horizontal", flip_Horizontal)
cv2.imshow("Both", flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("vertical_img.jpg", flip_vertical)
cv2.imwrite("horizontal_img.jpg", flip_Horizontal)
cv2.imwrite("Both_img.jpg", flip_both)
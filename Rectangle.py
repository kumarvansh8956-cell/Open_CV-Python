import cv2
img = cv2.imread("OpenCV.py/Test.jpg")

print(f"The shape of image:{img.shape}")
pt1 = (10,226) # top left point
pt2 = (300,426) # bottom right point
color = (0,0,266)
thickness = 5

cv2.rectangle(img,pt1,pt2,color, thickness)
cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Rectanglr.jpg",img)
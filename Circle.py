import cv2
img = cv2.imread("OpenCV.py/Test.jpg")

print(f"The shape of image:{img.shape}")
center = (148,256) 
redius = 135
color = (0,0,266)
thickness = 5

cv2.circle(img,center,redius,color, thickness)
cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("Circle.jpg",img)
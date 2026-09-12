import cv2
img = cv2.imread("OpenCV.py/Test.jpg")

print(f"The shape of image:{img.shape}")

pt1 = (10,426)     # left point
pt2 = (300,426)   # right point
color = (0,0,266)
thickness = 5

cv2.line(img,pt1,pt2,color, thickness)
cv2.imshow("line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# we can applied this directed too

cv2.line(img,pt1=(10,390),pt2=(300,390),color= (100,200,50), thickness= 8)
cv2.imshow("line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(
    "With_line.jpg",img
)
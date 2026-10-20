import cv2

# Load image
img_color = cv2.imread("Shape_1.jpg")

if img_color is None:
    print("ERROR/E: IMAGE NOT FOUND---")
else:
    gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    cont, hier = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img_color,cont, -1, [0,0,255],4)

    cv2.imshow("contour", img_color)
    cv2.waitKey()
    cv2.destroyAllWindows()
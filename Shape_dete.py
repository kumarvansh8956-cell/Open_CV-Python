import cv2

# Load image
img_color = cv2.imread("Shape_2.jpg")

if img_color is None:
    print("ERROR/E: IMAGE NOT FOUND---")
else:
    gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    cont, hier = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    

    for co in cont:
     espilon = 0.01*cv2.arcLength(co, True)
     approx = cv2.approxPolyDP(
                 co, espilon, True
         )
     corner = len(approx)
     if corner == 2:
        shape = "Line"
     elif corner == 3:
            shape = "Triangle"
     elif corner == 4:
            shape = "Quadrilateral"
     elif corner == 5:
            Shape = "Pentagon"
     elif corner > 5:
            shape = "Circle"
     else:
           shape = " Unknown"

     x, y, w, h = cv2.boundingRect(approx)
     cv2.drawContours(img_color,[approx], -1, [255,0.0],4)
    
     cv2.putText(img_color, shape, (x,y), cv2.FONT_HERSHEY_PLAIN, 1,[0,255,0])


    cv2.imshow("contour", img_color)
    cv2.waitKey()
    cv2.destroyAllWindows()
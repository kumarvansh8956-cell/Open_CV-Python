import numpy as np 
import cv2


page1= np.zeros((300,300), dtype= "uint8")
page2= np.zeros((300,300), dtype= "uint8")

circle =  cv2.circle(page1, (150,150),120, 255, -1 )
rect = cv2.rectangle(page2, (100,100), (275,275), 255, -1)

ANd =  cv2.bitwise_and(page2, page1)
Or =  cv2.bitwise_or(page1, page2)
NOt =  cv2.bitwise_not(page1)
Xor = cv2.bitwise_xor(page1, page2)
cv2.imshow("Circle", circle )
cv2.imshow("rectangle", rect)
cv2.imshow("AND",ANd)
cv2.imshow("OR", Or)
cv2.imshow("XOR", Xor)
cv2.imshow("NOT", NOt)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
For better result use grayscale
keep the height and weigth are same 
"""
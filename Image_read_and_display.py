import  cv2
# To read the image we use cv2.imread() method. this read image and store it into variable.
'''
Syntax:-
cv2.imread("Image_path", flag)
where flag is use to tell about how cv should read image
cv2.imread("image.jpg", 1)   # color   (it`s default )
cv2.imread("image.jpg", 0)   # grayscale
cv2.imread("image.png", -1)  # unchanged
          or
cv2.imread("image.png", cv2.IMREAD_COLOR)    (it`s default )
cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)
cv2.imread("image.png", cv2.IMREAD_UNCHANGED)
'''
img_color  = cv2.imread("pratice_image.jpg", 1)   
img_gray =cv2.imread("pratice_image.jpg", 0)   
img_unchange =cv2.imread("pratice_image.jpg", -1)

# To display the input image we use cv2.imshow() methods with new name
'''
Syntax:-
cv2.imshow("Image_new_Name", image_varible)

cv2.waitkey use to hold the image for specific amount of time
Example1 = cv2.waitkey(0) :- keep image hold until user did not press any key
Example2 = cv2.waitkey(1000) :- keep image hold for 1 second
Example3 = cv2.waitkey(5000) :- keep image hold for 5 second

cv2.destroyAllWindows() use to remove all window or images after displaying

'''

cv2.imshow("PicInColor",img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("PicInGray",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("PicInUnchange",img_unchange)
cv2.waitKey(0)
cv2.destroyAllWindows()

# To save the output image in our disk, we use cv2.imwrite() method
'''
Syntax:- 
cv2.imwrite(r"specific_location", image_varible)
              or
cv2.imwrite(r"NEw_name_AS_OUTPUT", image_varible)

'''
cv2.imwrite("output_image.png", img_gray)
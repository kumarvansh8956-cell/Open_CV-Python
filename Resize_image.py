import cv2
img = cv2.imread("OpenCV.py/Test.jpg")

# first get the size
print(f"the current size = {img.size}")
# resize
"""
To resizing a image we use cv2.resize()function. it can decrease or increase the size of the image according to our desire.

syntax:  resized = cv2.resize(img, (width, height), fx, fy, interpolation)

Here, img = original image varible
     (width, height) = parameter of new size
     fx = scaling parameter for X axis
     fy = scaling parameter for Y axis
     interpolation = This controls how OpenCV calculates the new pixels when resizing.
Common methonds

cv2.INTER_LINEAR ( decent for genral use)
cv2.INTER_AREA ( best for shrinking or downscaling )
cv2.INTER_CUBIC ( best for upscaling or expending but slow)
cv2.INTER_NEAREST ( fastest but can be blocking)
cv2.INTER_LANCZOS4 ( High-quality resizing but even slower)
     
Example =
resized = cv2.resize(
    img,
    (1000, 1000),
    interpolation=cv2.INTER_NEAREST
)

if you don't known exact width and height then you can use scalinf
     
Example =
        resized = cv2.resize(img, None, fx=0.5, fy=0.5)

fx = 1, fy = 1 => unchange or original size
fx = 2, fy = 2 => twice of original size
fx = 0.5, fy = 0.5 => half of original size
    
    
"""


new_img = cv2.resize(img , (300,300))
new_img2 = cv2.resize(img, None, fx= 0.25, fy= 0.25)

# new image size
print(f"the new size = {new_img.size}")
cv2.imshow("old image",img)
cv2.imshow("new image", new_img)
cv2.imshow("new image 2", new_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("resize_of_test.jpg",new_img)

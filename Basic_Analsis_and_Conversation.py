import cv2
img = cv2.imread("Test.jpg")

# to get the size or numbers of pixels of the images
print(f'The total numbeers of pixels in image is {img.size}')
# the datatype of image 
print(f'The datatype of the image is {img.dtype}')
# The Shape of the image
print(f'The shape of the image {img.shape}')
""" Or if you want them seprately"""
h,w,c = img.shape
print(f'The Height of image is {h} pixel',f"\n The Width of image is {w} pixel",f"\n The Color Chennel of image is {c}")

# for Number of dimension
print(f'Number of dimensions is {img.ndim}')


# The cv2.cvtColor() method is use for  changing an image from one color representation to another.
"""
Syntax:
cv2.cvtColor(image, conversion_code)

Example of color codes:-

| Conversion           | Meaning         |
| -------------------- | --------------- |
| `cv2.COLOR_BGR2GRAY` | BGR → Grayscale |
| `cv2.COLOR_BGR2RGB`  | BGR → RGB       |
| `cv2.COLOR_RGB2BGR`  | RGB → BGR       |
| `cv2.COLOR_BGR2HSV`  | BGR → HSV       |
| `cv2.COLOR_HSV2BGR`  | HSV → BGR       |
| `cv2.COLOR_BGR2LAB`  | BGR → LAB       |


"""
img2= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('the new',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
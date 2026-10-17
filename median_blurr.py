import cv2
image = cv2.imread("Test.jpg")
if image is None:
    print("Not Found")
else:
    new2 = cv2.medianBlur(image, 9)
    new3 = cv2.medianBlur(image, 13)
    new1 = cv2.medianBlur(image, 7)
    new4 = cv2.medianBlur(image, 3)
    new5 = cv2.medianBlur(image, 5)
    cv2.imshow("org",image)
    cv2.imshow("new1",new1)
    cv2.imshow("new2",new2)
    cv2.imshow("new3",new3)
    cv2.imshow("new4",new4)
    cv2.imshow("new5",new5)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
cv2.imwrite("blurr_img.jpg",new3)

"""
blur = cv2.medianBlur(img, 5)

- img — Input image.
- 5 — Kernel size (5 × 5 neighborhood). It must be a positive odd integer greater than 1.

Working
1. Select a neighborhood around a pixel.
2. Arrange the neighborhood's pixel values in ascending order.
3. Find the middle value (median).
4. Replace the center pixel with that median value.
5. Repeat for the image.



"""

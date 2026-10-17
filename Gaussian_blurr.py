import cv2
image = cv2.imread("Test.jpg")
if image is None:
    print("Not Found")
else:
    new1 = cv2.GaussianBlur(image, (31,31), 0)
    new2 = cv2.GaussianBlur(image, (31,31), 10)
    new3 = cv2.GaussianBlur(image, (15,33), 0)
    new4 = cv2.GaussianBlur(image, (13,13), 0)
    new5 = cv2.GaussianBlur(image, (7,7), 5)
    cv2.imshow("org",image)
    cv2.imshow("new1",new1)
    cv2.imshow("new2",new2)
    cv2.imshow("new3",new3)
    cv2.imshow("new4",new4)
    cv2.imshow("new5",new5)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


"""

cv2.GaussianBlur(inputimage, (x, y), sigma)

"""

"""
Parameters:

- inputimage — Input image.
- (x, y) — Kernel size (x × y pixels).
 sigma = strength of blurr
- 0 — Automatically calculates the Gaussian standard deviation (sigma).

Kernel size controls the neighborhood, while sigma controls the spread of Gaussian weights. Both influence the blur strength
Working:
1. A Gaussian kernel moves across the image.
2. Nearby pixels receive higher weights than distant pixels.
3. The weighted average replaces the original pixel value.
4. The result is a smoother, less noisy image.
Applications:
- Noise reduction.
- Image preprocessing.
- Smoothing images before edge detection.
- Reducing fine details in computer vision.
Key points:
- Larger kernels generally produce stronger blurring.
- Kernel dimensions should be positive odd numbers.
- Gaussian Blur smooths edges as well as noise.Parameters:
- img — Input image.
- (5, 5) — Kernel size (5 × 5 pixels).
- 0 — Automatically calculates the Gaussian standard deviation (sigma).
Working:
1. A Gaussian kernel moves across the image.
2. Nearby pixels receive higher weights than distant pixels.
3. The weighted average replaces the original pixel value.
4. The result is a smoother, less noisy image.
Applications:
- Noise reduction.
- Image preprocessing.
- Smoothing images before edge detection.
- Reducing fine details in computer vision.
Key points:
- Larger kernels generally produce stronger blurring.
- Kernel dimensions should be positive odd numbers.
- Gaussian Blur smooths edges as well as noise.




"""
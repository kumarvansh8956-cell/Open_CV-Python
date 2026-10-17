import cv2

img = cv2.imread("pratice_image.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("NOT FOUND!!!")

else:
    ret, thre =  cv2.threshold(img, 100, 225, cv2.THRESH_BINARY)

    cv2.imshow("OG", img)
    cv2.imshow("Threshold", thre)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(ret)

"""
thresholding is used to separate objects from their background based on pixel intensity.


syntax:-

retval, thresh = cv2.threshold(
    img, threshold_value, max_value, type
)

img — Input grayscale image.
threshold_value — Pixel intensity cutoff.
max_value — Value assigned to pixels that pass the threshold.
type — Thresholding method.
thresh — Resulting thresholded image.


With cv2.THRESH_BINARY and a threshold of 127:
- Pixel value greater than 127 → becomes 255 (white).
- Pixel value less than or equal to 127 → becomes 0 (black).

3. Types of thresholding
Method	What it does
|_________________________________________________________________________________________ |
|cv2.THRESH_BINARY	      |    Above threshold → white; otherwise black                   |
|cv2.THRESH_BINARY_INV	  |        Above threshold → black; otherwise white               |
|cv2.THRESH_TRUNC	      |    Values above threshold are clipped to the threshold        |   
|cv2.THRESH_TOZERO	      |    Values below or equal to threshold become zero             |    
|cv2.THRESH_TOZERO_INV	  |        Values above threshold become zero                     |     
 
4. Thresholding vs Canny
Thresholding: Separates pixels according to intensity.
Canny: Detects boundaries by analyzing intensity changes and gradient strength.


"""
import cv2

img = cv2.imread("pratice_image.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("NOT FOUND!!!")

else:
    edge =  cv2.Canny(img, 50, 225)

    cv2.imshow("OG", img)
    cv2.imshow("Canny_edge", edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

"""
syntax :- edges = cv2.Canny(image, threshold1, threshold2)

image — Input image, usually grayscale.
threshold1 — Lower threshold.
threshold2 — Upper threshold.

working
1. Noise reduction: Applies Gaussian blur to reduce unwanted noise.
2. Gradient calculation: Detects changes in image intensity to find possible edges.
3. Non-maximum suppression: Keeps thin edges by removing weaker neighboring pixels.
4. Double thresholding and edge tracking: Classifies edges using two thresholds and connects weak edges that are linked to strong edges.

Important: Canny uses hysteresis thresholding. Pixels above the upper threshold are strong edges, pixels between the thresholds are weak edges, and pixels below the lower threshold are rejected. Weak edges are retained when connected to strong edges.

A weak edge inside the threshold range is not automatically accepted. It must connect to a strong edge to survive hysteresis thresholding.


"""
# 👁️ OpenCV Learning Repository

A hands-on repository documenting my journey of learning **OpenCV with Python** and building a strong foundation in Computer Vision.

The goal of this repository is to understand how images and videos are represented, processed, analyzed, and transformed using OpenCV and NumPy.

---

## 🚀 About OpenCV

**OpenCV (Open Source Computer Vision Library)** is an open-source computer vision and machine learning library used for image processing, video analysis, object detection, feature extraction, and many other computer-vision tasks.

Official documentation: https://docs.opencv.org/

---

## 🎯 Learning Goals

* Understand how digital images are represented
* Learn OpenCV's basic image operations
* Understand BGR, RGB, Grayscale, HSV, LAB and YCrCb
* Work with pixels and image channels
* Perform image transformations
* Apply image filtering and smoothing
* Detect edges and shapes
* Work with contours
* Perform image segmentation
* Process videos and webcam streams
* Build practical Computer Vision projects

---

## 🧰 Technologies & Libraries

* 🐍 Python
* 👁️ OpenCV
* 🔢 NumPy
* 📓 Jupyter Notebook

---

## 📚 Topics Covered

### 1. Image Input & Output

* `cv2.imread()`
* `cv2.imshow()`
* `cv2.imwrite()`
* `cv2.waitKey()`
* `cv2.destroyAllWindows()`
* Image reading flags

### 2. Image Properties & Basic Analysis

* `shape`
* `size`
* `dtype`
* `ndim`
* Pixel access
* Pixel modification
* Image channels
* Region of Interest (ROI)
* NumPy array operations

### 3. Color Spaces & Conversion

* BGR
* RGB
* Grayscale
* HSV
* LAB
* YCrCb
* `cv2.cvtColor()`

Examples:

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

### 4. Geometric Transformations

* Image resizing
* Cropping
* Flipping
* Rotation
* Translation
* Affine transformations

Main functions:

```python
cv2.resize()
cv2.flip()
cv2.rotate()
```

### 5. Image Filtering & Smoothing

* Average Blur
* Gaussian Blur
* Median Blur
* Image noise reduction
* Custom filters

Main functions:

```python
cv2.blur()
cv2.GaussianBlur()
cv2.medianBlur()
```

### 6. Thresholding

* Binary thresholding
* Inverse thresholding
* Adaptive thresholding
* Otsu's thresholding

Main functions:

```python
cv2.threshold()
cv2.adaptiveThreshold()
```

### 7. Edge Detection

* Image gradients
* Sobel
* Laplacian
* Canny Edge Detection

Example:

```python
edges = cv2.Canny(gray, 100, 200)
```

### 8. Morphological Operations

* Erosion
* Dilation
* Opening
* Closing
* Morphological gradient

### 9. Contours

* Finding contours
* Drawing contours
* Contour area
* Perimeter
* Bounding rectangles
* Contour approximation

### 10. Histograms

* Image intensity distribution
* Histogram calculation
* Histogram visualization
* Histogram equalization

Main function:

```python
cv2.calcHist()
```

### 11. Video Processing

* Reading video files
* Writing video files
* Webcam capture
* Frame-by-frame processing
* FPS
* Video properties

Main class:

```python
cv2.VideoCapture()
```

### 12. Object Detection & Tracking

Coming soon:

* Color-based object detection
* Contour-based detection
* Object tracking
* Haar Cascade
* Modern object detection techniques

---

---

## 🧠 OpenCV + NumPy

OpenCV images loaded using `cv2.imread()` are represented as NumPy arrays.

For example:

```python
import cv2
import numpy as np

img = cv2.imread("image.jpg")

print(type(img))
print(img.shape)
print(img.dtype)
```

This makes NumPy extremely important for OpenCV because many low-level image operations involve manipulating arrays, pixels, and channels.

---

## 📈 Learning Progress

* [x] OpenCV installation
* [x] Reading images
* [x] Displaying images
* [x] Saving images
* [x] `waitKey()`
* [x] Image flags
* [x] Image shape and size
* [x] Pixel basics
* [x] BGR
* [x] RGB
* [x] Grayscale
* [x] HSV
* [x] LAB
* [x] YCrCb
* [ ] Image transformations
* [ ] Filtering
* [ ] Thresholding
* [ ] Edge detection
* [ ] Morphological operations
* [ ] Contours
* [ ] Histograms
* [ ] Video processing
* [ ] Object detection

---

## 🛠️ Projects

Practical projects will be added as I progress through OpenCV.

Planned projects include:

* 🎨 Color Detection
* 🖼️ Image Processing Tool
* 📹 Real-Time Webcam Processing
* 🔍 Shape Detection
* 👤 Face Detection
* 🎯 Object Tracking
* 🤖 Computer Vision + AI Projects

---

## 📖 Resources

* [OpenCV Documentation](https://docs.opencv.org/)
* [OpenCV-Python Tutorials](https://docs.opencv.org/4.13.0/d6/d00/tutorial_py_root.html)
* [OpenCV Image Processing Tutorials](https://docs.opencv.org/4.13.0/d2/d96/tutorial_py_table_of_contents_imgproc.html)

---

## 📌 Purpose

This repository is primarily a **learning and practice repository**.

I am using it to document my progress, experiment with OpenCV concepts, and build a strong foundation for future **Computer Vision and AI/ML projects**.

---

⭐ More topics and projects will be added as I continue learning Computer Vision.

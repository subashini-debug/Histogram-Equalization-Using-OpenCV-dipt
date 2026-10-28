# Histogram Equalization Using OpenCV (Grayscale & Color Images)
# Developed By: Farzana M
# Register No: 212225040087

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Read and display grayscale image
img_gray = cv2.imread('city.jpg', cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(img_gray, cmap='gray')
plt.title('original_image')
plt.show()

# 2. Histogram of grayscale image
plt.figure()
plt.hist(img_gray.ravel(), 256, range=[0, 256])
plt.title('Original Image')
plt.show()

# 3. Apply histogram equalization on grayscale image & plot histogram
img_eq = cv2.equalizeHist(img_gray)
plt.figure()
plt.hist(img_eq.ravel(), 256, range=[0, 256])
plt.title('Equalized Histogram')
plt.show()

# 4. Display equalized grayscale image
plt.figure()
plt.imshow(img_eq, cmap='gray')
plt.title('original image')
plt.show()

# 5. Read color image and perform histogram equalization on V channel (HSV)
img = cv2.imread('city.jpg', cv2.IMREAD_COLOR)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
img_eq = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)

# Display Original Color Image and Equalized Color Image
plt.figure(figsize=[12, 6])
plt.subplot(121)
plt.imshow(img[:, :, ::-1])
plt.title('Original Color Image')
plt.subplot(122)
plt.imshow(img_eq[:, :, ::-1])
plt.title('Equalized Image')
plt.show()

# 6. Display 2x2 grid comparing original vs equalized color image and histograms
plt.figure(figsize=[12, 10])
plt.subplot(221)
plt.imshow(img[:, :, ::-1])
plt.title('Original Color Image')
plt.subplot(222)
plt.imshow(img_eq[:, :, ::-1])
plt.title('Equalized Image')
plt.subplot(223)
plt.hist(img.ravel(), 256, range=[0, 256])
plt.title('Original Image')
plt.subplot(224)
plt.hist(img_eq.ravel(), 256, range=[0, 256])
plt.title('Histogram Equalized')
plt.show()

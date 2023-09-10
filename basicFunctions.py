import cv2
import numpy as np
import functions

kernel = np.ones((5, 5), np.uint8)
print(kernel)

path = "lena.png"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (13, 13), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow("Original", img)
cv2.imshow("Image Gray", imgGray)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Dilation", imgDilation)
cv2.imshow("Image Erosion", imgEroded)

print(img.shape)

width, height = 400, 400
imgResize = cv2.resize(img, (width, height))
print(imgResize.shape)
cv2.imshow("Img Resized", imgResize)

imgCrop = img[80:180, 60:180]
imgCrResize = cv2.resize(imgCrop, (img.shape[1], img.shape[0]))
cv2.imshow("Image Cropped", imgCrop)
cv2.imshow("Cropped Resized", imgCrResize)

cv2.waitKey(0)

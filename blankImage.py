import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

print(img)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)
cv2.line(img, (0, img.shape[0]), (img.shape[1], 0), (0, 255, 0), 2)
cv2.rectangle(img, (350, 200), (450, 300), (0, 0, 255), cv2.FILLED)
cv2.circle(img, (128, 256), 50, (255, 0, 0), 10)
cv2.putText(img, "Drawing Shapes in image", (40, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 150), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)

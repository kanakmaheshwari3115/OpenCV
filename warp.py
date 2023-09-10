import cv2
import numpy as np

img = cv2.imread("cards.jpg")

width, height = 100, 150

pts1 = np.float32([[246, 185], [399, 177], [252, 360], [414, 347]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOut = cv2.warpPerspective(img, matrix, (width, height))
# print(pts1)
# for x in range(0,4):
#     cv2.circle(img,(pts1[x][0],pts1[x][1]),3,(0,0,255),cv2.FILLED)

cv2.imshow("Original", img)
cv2.imshow("Output",imgOut)
cv2.waitKey(0)

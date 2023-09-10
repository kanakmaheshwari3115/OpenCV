import cv2
import numpy as np
import functions

kernel = np.ones((5, 5), np.uint8)

path = "lena.png"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (13, 13), 0)
imgCanny = cv2.Canny(img, 500, 500)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)


frameWidth = 640
frameHeight = 480

vid = cv2.VideoCapture(0)
vid.set(3, frameWidth)
vid.set(4, frameHeight)

while True:
    success, img = vid.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(img, (13, 13), 0)
    imgCanny = cv2.Canny(img, 500, 500)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
    imgEroded = cv2.erode(imgDilation, kernel, iterations=2)

    stackedImg = functions.stackimages(
        0.8, ([img, imgGray, imgBlur], [imgCanny, imgDilation, imgEroded])
    )
    cv2.imshow("Stacked Image", stackedImg)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break


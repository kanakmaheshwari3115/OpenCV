import cv2
import numpy as np

frameWidth=640
frameHeight=480

vid=cv2.VideoCapture(0)
vid.set(3,frameWidth)
vid.set(4,frameHeight)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VAL Min","HSV",0,255,empty)
cv2.createTrackbar("VAL Max","HSV",255,255,empty)


while True:
    success, img=vid.read()
    img=cv2.resize(img,(frameWidth,frameHeight))

    imgHsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min=cv2.getTrackbarPos("HUE Min","HSV")
    h_max=cv2.getTrackbarPos("HUE Max","HSV")
    s_min=cv2.getTrackbarPos("SAT Min","HSV")
    s_max=cv2.getTrackbarPos("SAT Max","HSV")
    v_min=cv2.getTrackbarPos("VAL Min","HSV")
    v_max=cv2.getTrackbarPos("VAL Max","HSV")

    lower = np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHsv, lower, upper)
    result=cv2.bitwise_and(img,img,mask=mask)

    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)

    hstack=np.hstack([img,mask,result])

    # cv2.imshow("Video",img)
    # cv2.imshow("Result",result)
    # cv2.imshow("Mask", mask)
    cv2.imshow("HSV Video", imgHsv)
    cv2.imshow("Stacked",hstack)


    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
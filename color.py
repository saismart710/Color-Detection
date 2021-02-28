import cv2
import numpy as np

def empty(a):
    pass


cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",400,200)
cv2.createTrackbar("Hue Min","Trackbars",13,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",21,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",40,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)
cv2.createTrackbar("Val Min","Trackbars",67,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

while True:
    img = cv2.imread("Res/lam.jpeg")
    imgr = cv2.resize(img,(300,200))
    imgHSV = cv2.cvtColor(imgr,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
    v_min = cv2.getTrackbarPos("Val Min","Trackbars")
    v_max = cv2.getTrackbarPos("Val Max","Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(imgr,imgr,mask=mask)


    cv2.imshow("Image",imgr)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("MASK",mask)
    cv2.imshow("RESULT",imgResult)
    cv2.waitKey(1)
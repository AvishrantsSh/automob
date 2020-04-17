import cv2
import numpy as np

def epmty(a):
    pass

path = "res/lambo.PNG"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,280)
cv2.createTrackbar("HueMin","TrackBars",0,179,epmty)
cv2.createTrackbar("HueMax","TrackBars",179,179,epmty)
cv2.createTrackbar("SatMin","TrackBars",0,255,epmty)
cv2.createTrackbar("SatMax","TrackBars",255,255,epmty)
cv2.createTrackbar("ValMin","TrackBars",0,255,epmty)
cv2.createTrackbar("ValMax","TrackBars",255,255,epmty)


while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HueMin","TrackBars")
    h_max = cv2.getTrackbarPos("HueMax", "TrackBars")
    s_min = cv2.getTrackbarPos("SatMin", "TrackBars")
    s_max = cv2.getTrackbarPos("SatMax", "TrackBars")
    v_min = cv2.getTrackbarPos("ValMin", "TrackBars")
    v_max = cv2.getTrackbarPos("ValMax", "TrackBars")

    print(h_max,h_max,s_min,s_max,v_min,v_max)
    LOWER = np.array([h_min,s_min,v_min])
    UPPER = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imgHSV,LOWER,UPPER)

    cv2.imshow("ORiginal",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)

    cv2.waitKey(1)
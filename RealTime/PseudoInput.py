import cv2
import lib_rad as lib

cam = cv2.VideoCapture("/home/avishrant/Desktop/vid1.mp4")
#cam = cv2.VideoCapture(0)

if not(cam.isOpened()):
    print("Error Accessing Camera Object")
else:
    while True:
        ret,frame = cam.read()
        radius = lib.ldetect(frame)
        cv2.imshow('Original',frame)
        frame = radius.findrad()
        cv2.imshow('Edited',frame)
        k = cv2.waitKey(1)
        if k+1:
            break
    
    cam.release()
    cv2.destroyAllWindows()
import cv2
import lib_rad as lib

cam = cv2.VideoCapture(0)

if not(cam.isOpened()):
    print("Error Accessing Camera Object")
else:
    while True:
        ret,frame = cam.read()
        radius = lib.radius(frame)
        radius.findrad()
        cv2.imshow('preview',frame)
        if cv2.waitKey(1):
            break
    
    cam.release()
    cv2.destroyAllWindows()
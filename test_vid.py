import cv2
import lib_rad_gps as lib

cam = cv2.VideoCapture("/home/avishrant/Desktop/nfs.mp4")
cam.set(cv2.CAP_PROP_FPS, 30)

if not(cam.isOpened()):
    print("Error Accessing Camera Object")
else:
    while True:
        ret,frame = cam.read()
        radius = lib.radius(frame)
        radius.findrad()
        cv2.imshow('preview',frame)
        if cv2.waitKey(1) != -1:
            break
    
    cam.release()
    cv2.destroyAllWindows()
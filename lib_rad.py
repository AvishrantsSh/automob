#Library for determining the Circle Radius and Other Parameters

import cv2
import numpy as np

class radius(object):
    dim = []
    min = 50
    max = 0
    def __init__(self,path):
        self.img = cv2.imread(path)
        
    def findrad(self):
        cimg = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        cimg = cv2.blur(cimg,(3,3))
        self.getParam(cimg)
        circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,5,param1=80,param2=50,minRadius=radius.min ,maxRadius=radius.max)
        
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(self.img,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(self.img,(i[0],i[1]),2,(0,0,255),3)
        print(len(*circles))
           
        self.imshow()

    def getParam(self,cimg):
        mcount = 100
        for x in range(radius.min,100):
            circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,5,param1=80,param2=50,minRadius=radius.min ,maxRadius=x)
            if circles is not None and len(*circles) < mcount:
                mcount = len(*circles)
                radius.max = x


    def imshow(self):
        cv2.imshow('Image' , self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
#Library for determining the Circle Radius and Other Parameters

import cv2
import numpy as np

class radius(object):
    dim = []
    max = 150
    #min = 60
    def __init__(self,img):
        self.img = img
        
    def findrad(self):
        cimg = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        cimg = cv2.blur(cimg,(3,3))
        self.getParam(cimg)
        
    def getParam(self,cimg):

        for x in range(10,radius.max,10):
            circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,10,param1=85,param2=80,minRadius=x ,maxRadius=radius.max)
            if circles is not None and len(*circles)  < 5:
                h,k,r=0,0,0
                for i in circles[0,:]:
                    h = i[0]
                    k = i[1]
                    r = i[2]
                    # draw the outer circle
                    cv2.circle(self.img,(h,k),r,(0,255,0),1)
                    # draw the center of the circle
                    cv2.circle(self.img,(h,k),2,(0,0,255),2)
                    
              
    
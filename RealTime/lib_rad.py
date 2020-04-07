
#Library for determining the Circle ldetect and Other Parameters

import cv2
import numpy as np

class ldetect(object):
    pimg = []
    dim = []
    color = (255,0,0)
    output = (1280,720)
    def __init__(self,img):
        self.img = img
        ldetect.dim=img.shape
        
        
    def findrad(self):
        self.preimg()
        #self.mask()
        ldetect.pimg = self.change_perspective(ldetect.pimg)
        # ldetect.pimg = cv2.Sobel(ldetect.pimg,cv2.CV_64F,1,0,ksize=5)
        ldetect.pimg = self.inv_perspective(ldetect.pimg)
        self.getlane()
        return self.img

    def preimg(self):
        ldetect.pimg = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        ldetect.pimg = cv2.GaussianBlur(ldetect.pimg, (5, 5), 0)  
        ldetect.pimg = cv2.Canny(ldetect.pimg, 50, 150)
                    
                    
    
    def mask(self):
        h = ldetect.dim[0]
        w = ldetect.dim[1]
        imgmask = np.zeros_like(ldetect.pimg) 
        vertices = np.array([[
            (0, h),(0.4*w, 0.6*h),(0.6*w, 0.6*h),(w,h)
            ]] , dtype=np.int32)
        
        cv2.fillPoly(imgmask, vertices,255)
        ldetect.pimg = cv2.bitwise_and(imgmask,ldetect.pimg)
    


    def change_perspective(self,img):
        h = ldetect.dim[0]
        w = ldetect.dim[1]
        pts1 = np.float32([[0.40*w,0.65*h],[0.60*w,0.65*h],[w,h],[0,h]])
        pts2 = np.float32([[0,0],[1,0],[1,1],[0,1]])
        pts2 = pts2*np.float32(ldetect.output)
        mat = cv2.getPerspectiveTransform(pts1,pts2)
        img = cv2.warpPerspective(img,mat,ldetect.output)
        return img
        
    
    def convert(self):
        ldetect.pimg = np.absolute(ldetect.pimg)
        ldetect.pimg = np.uint8(ldetect.pimg)

    def inv_perspective(self,img):
        h = ldetect.dim[0]
        w = ldetect.dim[1]
        pts1 = np.float32([[0.40*w,0.65*h],[0.60*w,0.65*h],[w,h],[0,h]])
        pts2 = np.float32([[0,0],[1,0],[1,1],[0,1]])
        pts2 = pts2*np.float32(ldetect.output)
        mat = cv2.getPerspectiveTransform(pts2,pts1)
        img = cv2.warpPerspective(img,mat,ldetect.output)
        return img

    def getlane(self):
        lines = cv2.HoughLinesP(ldetect.pimg,rho=6,theta=np.pi / 60,threshold=160,lines=np.array([]),minLineLength=40,maxLineGap=25)
        if lines is not None:
            for x in lines:
                for x1,y1,x2,y2 in x:
                    cv2.line(self.img,(x1,y1),(x2,y2),ldetect.color,2)

        
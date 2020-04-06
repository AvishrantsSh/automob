import lib_rad_gps as rlib
import cv2

path = "/home/avishrant/GitRepo/automob/TestData/road1.jpeg"
img = cv2.imread(path)

radius = rlib.radius(img)
radius.findrad()

cv2.imshow('Preview',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

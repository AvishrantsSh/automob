from lib_rad import radius
from easygui import fileopenbox
import cv2

#img_path = fileopenbox()
origimg = cv2.imread("/home/avishrant/GitRepo/automob/TestData/circle.png")
(thresh, img) = cv2.threshold(cv2.cvtColor(origimg, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)

radius = radius(img)
radius.findrad()
assert len(img) > 0
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

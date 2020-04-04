#Library for determining the Circle Radius and Other Parameters
class radius(object):
    dim = []

    def __init__(self,img):
        self.img = img
        self.coord = []
        radius.dim = img.shape


    def findrad(self):
        print(radius.dim)
        x = 0
        while x < radius.dim[0]:
            y = 0
            while y < radius.dim[1]:
                if self.img[x][y] == 0:
                    self.coord.append([x,y])
                    while self.img[x][y] == 0 :
                        y += 1
                y += 1
            x += 1

        print("Got Circle Info")
                
        print("Proceeding")

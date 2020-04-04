#Library for determining the Circle Radius and Other Parameters
class radius(object):
    dim = []

    def __init__(self,img):
        self.img = img
        radius.dim = img.shape

    def findrad(self):
        self.binarray()
        print(radius.dim)

    def binarray(self):
        arr = []
        for x in range(radius.dim[1]):
            tmp = []
            for y in range(radius.dim[0]):
                if self.img[x][y] == 0:
                    tmp.append(0)
                else:
                    tmp.append(1)
            arr.append(tmp)
        
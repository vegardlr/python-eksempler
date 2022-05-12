import numpy as np

class Frame:
    def __init__(self,x,y,d=10,label='',data=None):
        self.x = x
        self.y = y
        self.d = d
        self.data = data
        self.label = label
        self.xframe = [x-d,x-d,x+d,x+d,x-d]
        self.yframe = [y-d,y+d,y+d,y-d,y-d]
        self.pixel_area = 4*d*d
    
    def crop(self,data):
        x = self.x
        y = self.y
        d = self.d
        return data[y-d:y+d,x-d:x+d]

    def peak(self,data):
        x = self.x
        y = self.y
        d = self.d
        return np.max(data[y-d:y+d,x-d:x+d])

    def flux(self,data):
        x = self.x
        y = self.y
        d = self.d
        return np.sum(data[y-d:y+d,x-d:x+d])/self.pixel_area

    def plotframe(self,style='r-'):
        return self.xframe,self.yframe


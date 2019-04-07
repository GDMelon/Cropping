from PIL import Image
class cropImg:
    def __init__(self, img, y_move=0,x_move=0,h_crop_size=1,w_crop_size=1):
        self.img = img
        self.img_h, self.img_w = self.img.getsize()
        self.h_size = h_crop_size
        self.w_size = w_crop_size
        self.max_h,self.max_w = self._crop_size()
        self.y = y_move
        self.x = x_move

    def _crop_size(self):
        h_size = int(self.img_h / self.h_size)
        w_size = int(self.img_w / self.w_size)
        return h_size,w_size

    def getBox(self):
        boxset = (0+self.x,0 +self.y, self.max_h + self.x,self.max_w+self.y)
        return boxset

    def crop(self):
        return self.img.crop(self.getBox())

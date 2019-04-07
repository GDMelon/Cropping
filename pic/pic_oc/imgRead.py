from PIL import Image


class img:

    def __init__(self, path):
        self.path = path
        self.img = self._readImg()
        self.img_w,self.img_h = self.img.size

    def _readImg(self):
        img = Image.open(self.path)
        return img

    def show(self):
        img.show(self.img)

    def type(self):
        print("当前文件的类型为：")
        print(type(self.img))

    def getsize(self):
        return self.img_h, self.img_w

    def Img(self):
        return self.img







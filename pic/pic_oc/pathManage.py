import os

class pathman():
    def __init__(self, path):
        self.path = path

    def getpath(self,):
        print('开始执行getpath')
        fileLst = os.listdir(self.path)
        imgLst = []
        for i in fileLst:
            if self._extension(i) == ".JPG":
                imgPath = os.path.join(self.path, i)
                imgLst.append(imgPath)

        return imgLst

    def _extension(self, filepath):
        lst = os.path.splitext(filepath)
        return lst[-1]

    def showAction(self):
        print("成功获取路径")

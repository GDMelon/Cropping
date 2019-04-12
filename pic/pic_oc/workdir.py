import os

def setWorkDir():
    codePath = os.getcwd()
    pictureSavingDirectory = "startdir"

    imglst = []

    upperDirectory = os.path.dirname(codePath)

    # 存放图片的初始目录
    workDirectory = os.path.join(upperDirectory, pictureSavingDirectory)

    return workDirectory


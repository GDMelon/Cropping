import os
from PIL import Image
import  workdir,itemSelect,cropBox,pictureCrop,ADmode,cropExe

cropBoxSet = ""

print("输入图片存放的目录：")
startdir = input()
# print(startdir)
if startdir == "":
    print("使用默认工作目录")
    workDirectory = workdir.setWorkDir()
else:
    workDirectory = startdir
print("工作目录为：")
print(workDirectory)

# 目录中文件所有的文件
imglst = os.listdir(workDirectory)

print("文件夹中待处理的内容：")
itemlst = itemSelect.itemSelect(imglst)
print(itemlst)

print("选择调试模式--输入 AD")
print("选择批量处理--输入 WR")
worktype = input()


if worktype == "AD":
    file = os.path.join(workDirectory,itemlst[-1])
    img = Image.open(file)
    imgWeight, imgHeight = img.size
    print("选择剪裁方式")
    print("中心剪裁 -- C")
    print("边缘剪裁 -- S")
    cropType = input()
    if cropType == "C":
        print("待处理图片尺寸为："+ str(img.size))
        # scale = input("剪裁范围(0.0~1.0): ")
        # scale = float(scale)
        # print("输入偏移值：")
        # inputX = input("X轴方向偏移：")
        # if inputX == "":
        #     inputX = 0.0
        # inputY = input("Y轴方向偏移：")
        # if inputY == "":
        #     inputY = 0.0
        cropPara = cropExe.cropexe(file,img)
        takeThePara = input("是否使用当前参数：")
        if takeThePara == "是":
            cropBoxSet = cropPara
        else:
            print("当前设置的参数为：")
            print(cropPara)
            cropPara = cropExe.cropexe(file,img)

    elif cropType == "S":
        pass



        # boxset = cropBox.midCrop()
elif worktype== "WR":
    for i in itemlst:
        file = os.path.join(workDirectory,i)
        img = Image.open(file)
        img.pictureCrop.crop(file,cropBoxSet)
        # 保存路径
        # 在工作路径下新建保存路径
        # 获得当前文件名的前缀+已经编辑的标识
else:
    print("输入错误")


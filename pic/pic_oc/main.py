import os
from PIL import Image

# 工作路径
import workdir
# 筛选调整对象
import itemSelect
# 调试模式
import adjustMode
# 批量处理
import processMode

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
    # 重写调试模式
    cropType,boxPara = adjustMode.cropAdjust(file)
    print("当前剪裁模式为："+ cropType)
    print("\n")
    print("是否进行批量处理？：")
    judePara = input()
    if judePara == "是":
        processMode.cropProcess(workDirectory,itemlst,boxPara)

    else:
        print("滚！")

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


# 批量处理图片
# 获得工作目录的路径和经过筛选的项目
# 对图片进行处理

import os
from PIL import Image

def cropProcess(workDirectory,itemlst,boxSet):
    outputdir = os.path.join(workDirectory,"output")
    count = 1
    total = len(itemlst)
    for i in itemlst:
        print(str(count)+ "in" + str(total))
        file = os.path.join(workDirectory,i)
        img = Image.open(file).crop(boxSet)
        count += 1
        img.save(outputdir)
    print("完成")

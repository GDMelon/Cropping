from PIL import Image
import setCropPara,cropBox,pictureCrop

imgSize = ()

def _rePara(file, cropType,imgSize1):
    boxPara = _getPara(imgSize1)
    img = pictureCrop.crop(file, boxPara)
    img.show()
    print("参数是否可以使用:")
    Jude = input()
    if Jude == "是":
        return cropType,boxPara
    else:
        _rePara()

def _getPara(imgSize):
    scale, offsetTuple = setCropPara.paraSet()
    boxPara = cropBox.midCrop(imgSize,scale,offsetTuple)
    return boxPara


def cropAdjust(file):
    img = Image.open(file)
    imgSize=  img.size

    print("选择剪裁方式")
    print("中心剪裁 -- C")
    print("边缘剪裁 -- S")
    cropType = input()
    if cropType == "C":
        #设置剪裁参数
        boxPara = _getPara(imgSize)
        img = pictureCrop.crop(file,boxPara)
        img.show()
        print("参数是否可以使用:")
        Jude = input()
        if Jude == "是":
            return cropType,boxPara
        else:
            _rePara(file,cropType,imgSize)
    elif cropType == "S":
        pass
    else:
        pass






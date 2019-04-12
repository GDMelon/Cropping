import ADmode
import cropBox,pictureCrop

def cropexe(file,img):
    scale, moveTuple = ADmode.paraSet()
    if scale <= 1.0 and scale >= 0.0:
        boxset = cropBox.midCrop(img.size, scale, moveTuple)
        img = pictureCrop.crop(file, boxset)
        img.show()
        print("图片展示：")
        return boxset
    else:
        print("输入超出范围")
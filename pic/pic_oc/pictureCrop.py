from PIL import Image

def crop(file, boxset):
    img = Image.open(file)
    # img.show()
    img_w, img_h = img.size

    # 从左上角开始 ，x1,y1,x2,y2
    # boxset = (0,0,img_w/2,img_h/2)
    # print(boxset)
    img = img.crop(boxset)
    return img
    # print(img_w,img_h)
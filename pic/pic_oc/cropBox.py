def midCrop(tuple1, scale,tuple2):
    imgW, imgH = tuple1
    movX, movY = tuple2
    cenX = int(imgW/2) + int(movX)
    cenY = int(imgH/2) + int(movY)
    chaX = int(cenX * scale)
    chaY = int(cenY * scale)
    box = (cenX-chaX,cenY-chaY,cenX+chaX,cenY+chaY)
    return box

def sidCrop():
    pass

def paraSet():
    scale = input("剪裁范围(0.0~1.0): ")
    scale = float(scale)
    print("输入偏移值：")
    inputX = input("X轴方向偏移：")
    if inputX == "":
        inputX = 0.0
    inputY = input("Y轴方向偏移：")
    if inputY == "":
        inputY = 0.0
    return scale,(inputX,inputY)
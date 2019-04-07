import imgRead
import pathManage
import crop_PIL

# path = '/Users/Bran/Desktop/test_file'
path = r'C:\Users\Administrator\Desktop\test_file'

mod = 'freedom'

# mod = 'centre'


def main(path):
    print('输入目标路径')
    path_input = input()
    if path_input == "\n":
        path_input = path

    print('执行路径是：'+ path_input )
    # print('执行这里：')
    img_path = pathManage.pathman(path_input)
    img_dir = img_path.getpath()
    print('当前目录中有如下.JPG')
    print(img_dir)

    # img_path.showAction()
    # print('\n')

    for i in img_dir:
        img = imgRead.img(i)
        # img.type()
        print(img.getsize())







if __name__ == '__main__':
    print('开始执行主程序')
    main(path)
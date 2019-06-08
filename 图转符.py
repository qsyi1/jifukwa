print('工号1810108407为恁服务，谢绝野蛮人借鉴，qqqxx!')
import matplotlib.pyplot as plt

show_height = int(input('那么首先能告诉我字符画的高度吗:'))              
show_width = int(input('输入宽度，请:'))
#这两个数字是可以调的，非常文明，，，

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#生成一个ascii字符列表
char_len = len(ascii_char)

newpic = input('在?把你jpg格式图片文件名交了，请:')
pic = plt.imread(newpic)
#使用plt.imread方法来读取图像，对于彩图，则生成size = heigth*width*3的图像。matplotlib 中色彩排列是R G B，opencv的cv2中色彩排列是B G R。

pic_height,pic_width,_ = pic.shape
#获取图像的高和宽，，，

gray = 0.2126 * pic[:,:,0] + 0.7152 * pic[:,:,1] + 0.0722 * pic[:,:,2]
#RGB转灰度图的公式:gray = 0.2126 * r + 0.7152 * g + 0.0722 * b。

#思路：根据灰度值，映射到相应的ascii_char。
for i in range(show_height):
    #根据比例映射到对应的像素。
    y = int(i * pic_height / show_height)
    text = ""
    for j in range(show_width):
        x = int(j * pic_width / show_width)
        text += ascii_char[int(gray[y][x] / 256 * char_len)]
    print(text)
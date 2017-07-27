# test_qq_pic.py
# coding: utf-8
'''
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。 类似于图中效果
往Jellyfish.jpg上叠加start.png
难点：
1. 将两个图片混合
2. 生成随机数字的图片
'''

# import Image
# im = Image.open(r'C:\Users\Public\Pictures\Sample Pictures\Jellyfish.jpg')
# # 获得图像尺寸:
# w, h = im.size
# # 缩放到50%:
# im.thumbnail((w//2, h//2))
# # 把缩放后的图像用jpeg格式保存:
# im.save('C:\Users\Public\Pictures\Sample Pictures\Jellyfish_new.jpg', 'jpeg')

from PIL import Image
import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndNum():
    return random.randint(1, 90)

# 随机颜色1:
def RedColor():
    return (255,0,0)
def WhiteColor():
	return (255,255,255)



# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=WhiteColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndNum(), font=font,fill=RedColor()) # 这里调用draw.text()有问题
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save(r'C:\Users\Public\Pictures\Sample Pictures\start.jpg', 'jpeg');


#加载底图
base_img = Image.open(r'C:\Users\Public\Pictures\Sample Pictures\start.jpg')
# 可以查看图片的size和mode，常见mode有RGB和RGBA，RGBA比RGB多了Alpha透明度
# print base_img.size, base_img.mode
box = (166, 64, 320, 337)  # 底图上需要P掉的区域

#加载需要P上去的图片
tmp_img = Image.open(r'C:\Users\Public\Pictures\Sample Pictures\start.png')
#这里可以选择一块区域或者整张图片
#region = tmp_img.crop((0,0,304,546)) #选择一块区域
#或者使用整张图片
region = tmp_img

#使用 paste(region, box) 方法将图片粘贴到另一种图片上去.
# 注意，region的大小必须和box的大小完全匹配。但是两张图片的mode可以不同，合并的时候回自动转化。如果需要保留透明度，则使用RGMA mode
#提前将图片进行缩放，以适应box区域大小
# region = region.rotate(180) #对图片进行旋转
region = region.resize((box[2] - box[0], box[3] - box[1]))
base_img.paste(region, box)
#base_img.show() # 查看合成的图片
base_img.save(r'C:\Users\Public\Pictures\Sample Pictures\output.png') #保存图片



# 随机字母:

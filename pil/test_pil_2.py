# test_pil_2.py
# coding: utf-8
'''
add a text under a picture

'''
from PIL import Image, ImageDraw, ImageFont
import math
import sys
print sys.getdefaultencoding()


text=u"尽管曾作为皇家猎场而存在，意大利大帕拉迪索国家公园一直保留着其野性的一面。"

# why cannot output Chinese? u to force CHANGED...

def make_text_image(width, white, text, save_path, mode = "rgb"):
 """
 生成一个文字图形, white=1，表示白底黑字，否则为黑底白字
 """

 # 字体可能要改
 # linux查看支持的汉字字体 # fc-list :lang=zh
 ft = ImageFont.truetype("/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf", 15)
 w, h = ft.getsize(text)

 # 计算要几行
 lines = math.ceil(w / width) + 1
 height = h * lines

 # 一个汉字的宽度
 one_zh_width, h = ft.getsize("中")

 if len(mode) == 1: # L, 1
  background = (255)
  color = (0)
 if len(mode) == 3: # RGB
  background = (255, 255, 255)
  color = (0,0,0)
 if len(mode) == 4: # RGBA, CMYK
  background = (255, 255, 255, 255)
  color = (0,0,0,0)

 newImage = Image.new(mode, (int(width), int(height)), background if white else color)
 draw = ImageDraw.Draw(newImage)

 # 分割行
 text = text + " " #处理最后少一个字问题
 text_list = []
 start = 0
 end = len(text) - 1
 while start < end:
  for n in range(end):
   try_text = text[start:start+n]
   w,h = ft.getsize(try_text)
   if w + 2*one_zh_width > width:
    break
  text_list.append(try_text[0:-1])
  start = start + n - 1;

 # print(text_list)

 i = 0
 for t in text_list: 
  draw.text((one_zh_width, i * h), t, color if white else background, font=ft)
  i = i + 1

 newImage.save(save_path);


def resize_canvas(org_image="2.jpg", add_image="222.jpg", new_image_path="save2.jpg"):

 org_im = Image.open(org_image)
 org_width, org_height = org_im.size

 mode = org_im.mode

 make_text_image(org_width, 0, text, "222.jpg", mode)

 add_im = Image.open(add_image)
 add_width, add_height = add_im.size

 mode = org_im.mode

 newImage = Image.new(mode, (org_width, org_height + add_height))

 newImage.paste(org_im, (0, 0, org_width, org_height))
 newImage.paste(add_im, (0, org_height, add_width, add_height + org_height))
 newImage.save(new_image_path)

resize_canvas()
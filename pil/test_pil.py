# test_pil.py
# coding: utf-8

import os, sys, fnmatch
import Image, ImageDraw, ImageFont
'''
where to get FONTS?
locate .ttf (run this command and see how many fonts have?)
'''
def process_picture(filename):
  seq = os.path.split(filename)[-1][0].upper()
  img = Image.open(os.path.join(input_dir, filename))

  draw = ImageDraw.Draw(img)

  # 在右下角画白底黑框圆圈
  draw.ellipse((215, 215, 235, 235), outline='black', fill='white')

  # 将字母序号写入到圆圈内
  font = ImageFont.truetype('/usr/share/fonts/truetype/tlwg/Waree-Bold.ttf', 20)

  # 计算文字居中的位置
  text_size = draw.textsize(seq, font)
  x = (20 / 2) - (text_size[0] / 2)
  y = (20 / 2) - (text_size[1] / 2)

  # 字母偏移量
  offsets = {'A': 1, 'B': 1, 'E': 1, 'D': 2}
  offset = offsets.get(seq, 0)
  draw.text((215 + x + offset, 215 + y), seq, font=font, fill='black')

  # save image
  img.save(os.path.join(output_dir, filename), 'JPEG')

if __name__ == '__main__':
  if len(sys.argv) < 3:
    print 'Usage: python drawseq.py <input_dir> <output_dir>'
    sys.exit(1)

  input_dir, output_dir = sys.argv[1:3] 
  os.path.exists(output_dir) or os.makedirs(output_dir)

  for filename in os.listdir(input_dir):
    if fnmatch.fnmatch(filename.lower(), '*.jpg'):
      process_picture(filename)

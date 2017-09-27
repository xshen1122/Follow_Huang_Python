# test_gif.py
# coding: utf-8
'''
Image对象有open方法却没有close方法，如果打开图片，判断图片高度和宽度，
判断完成后希望删除或者给图片改名，是无法操作的，这段代码可以解决这个问题，
注意open函数打开图片文件要使用二进制方式，及参数使用'rb'，
有的文章给出的只有个'r'参数，Image是无法open的

''' 
import os 
import Image 
fileName = '/home/real/Pictures/1.jpg' 
fp = open(fileName,'rb') 
im = Image.open(fp) 
fp.close() 
x,y = im.size 
print x, y # 550x366

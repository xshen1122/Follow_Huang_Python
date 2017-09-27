# test_matplot.py
# coding: utf-8
'''
http://reverland.org/python/2012/09/07/matplotlib-tutorial/
Chinese version for matplotlib

'''
import matplotlib.pyplot as plt
import numpy as nu
pp = [32,45,29,101,98]
y=pp  # 设置y轴数据，以数组形式提供

x=len(y)           # 设置x轴，以y轴数组长度为宽度
x=range(x)      # 以0开始的递增序列作为x轴数据

plt.ylabel('some values')
plt.plot(x,y)  #  只提供x轴，y轴参数，画最简单图形
plt.show()

'''
define cavas size
plot 4 pictures on 221, 222, 223, 224
'''

plt.figure(figsize=(8,8),dpi=80)
plt.subplot(221)
plt.plot(x,y)
plt.subplot(222)
plt.plot(x,y)
plt.subplot(223)
plt.plot(x,y)
plt.subplot(224)

plt.xlim(0,4)
plt.ylim(0,200)
plt.xticks(nu.linspace(0,4,1,endpoint=True))
plt.yticks(nu.linspace(0,200,10,endpoint=True))
plt.plot(x,y,color='red',linewidth=2.5,linestyle='-')
plt.show()

'''
plt.xticks()：设置x轴刻度的表现方式

plt.xlim()：设置x轴刻度的取值范围
'''
'''

plt.plot(y,xx,color='red',linewidth=2.5,linestyle='-') 
# color参数设置曲线颜色，linewidth设置曲线宽度，linestyle设置曲线风格
'''
'''
 plt.ylabel('some numbers')
'''
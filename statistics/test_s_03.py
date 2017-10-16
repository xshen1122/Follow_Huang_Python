# test_s_03.py
# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
'''
相对用于平均数和标准差这两个数字，图表能够更形象有效地描述数据分布特征和数据集的特征。

用python计算和画图，numpy 中的histogram可以计算直方图分布，
matplotlib.pyplot中的hist可以计算直方图和画图。
用matplotlib绘图模块可以绘制柱状图、条形图、曲线、饼图等各种图形。
refer to http://www.jb51.net/article/104924.htm
'''
def histPic():
	data = [47,10,31,25,20,  
	        2,11,31,25,21,  
	        44,14,15,26,21,  
	        41,14,16,26,21,  
	        7,30,17,27,24,  
	        6,30,17,27,24,  
	        35,32,15,29,23,  
	        38,33,19,28,20,  
	        35,34,18,29,21,  
	        36,32,16,27,20] 
	a,b = np.histogram(data,bins=[0,5,10,15,20,25,30,35,40,45,50]) 
	print a  
	print b  

	plt.hist(data,bins=[0,5,10,15,20,25,30,35,40,45,50])  
	plt.show()  


# --- bar Pic ------------------------
def barPic():
	data = [5, 20, 15, 25, 10]

	plt.bar(range(len(data)), data)
	plt.show()
def barPic1():
	data = [5, 20, 15, 25, 10]

	plt.bar([0.3, 1.7, 4, 6, 7], data, width=0.6, bottom=[10, 0, 5, 0, 5])
	plt.show()
def barLeftRightPic():
	size = 5
	x = np.arange(size)
	a = np.random.random(size)
	b = np.random.random(size)
	c = np.random.random(size)

	total_width, n = 0.8, 3
	width = total_width / n
	x = x - (total_width - width) / 2

	plt.bar(x, a, width=width, label='a',color='red')
	plt.bar(x + width, b, width=width, label='b',color='green')
	plt.bar(x + 2 * width, c, width=width, label='c',color='blue')
	plt.legend()
	plt.show()
def barUpDownPic():
	size = 5
	x = np.arange(size)
	a = np.random.random(size)
	b = np.random.random(size)

	plt.bar(x, a, label='a',color='yellow')
	plt.bar(x, b, bottom=a, label='b',color='black')
	plt.legend()
	plt.show()

def barHirozon():

	data = [5, 20, 15, 25, 10]

	plt.barh(range(len(data)), data)
	plt.show()
def barPlus():
	a = np.array([5, 20, 15, 25, 10])
	b = np.array([10, 15, 20, 15, 5])

	plt.barh(range(len(a)), a)
	plt.barh(range(len(b)), -b)
	plt.show()

#--------------Pie---------------
def piePic():
	labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
	sizes = [15, 30, 45, 10]
	colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
	explode = (0, 0.1, 0, 0) # only "explode" the 2nd slice (i.e. 'Hogs')

	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
	  autopct='%1.1f%%', shadow=True, startangle=90)

	# Set aspect ratio to be equal so that pie is drawn as a circle.
	plt.axis('equal')
	plt.show()


if __name__ == '__main__':
	piePic()
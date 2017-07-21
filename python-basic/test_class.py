# test_class.py
# coding: utf-8
'''
类，多态，继承
定义一个Point类 - 各种方法，+
'''

class Point:
	def __init__(self,x,y):
		self.x, self.y = x, y
	def set(self,x,y):
		self.x, self.y = x,y 
	def __f():
		pass
	def __str__(self):
		return 'I am a Point, x is {0}, y is {1}'.format(self.x, self.y)
	def __add__(self,other):
		return Point(self.x+other.x, self.y+other.y) # 重载了+运算符

# print type(Point)
# print dir(Point) #['__doc__', '__init__', '__module__', 'set']
# p = Point(10,10)
# print type(p)
# print dir(p)
# print p
# t = Point(20,20)
# print p+t
import math
class Shape:
	def area(self):
		return 0.0

class Circle(Shape):
	def __init__(self, r=0.0):
		self.r = r
	def area(self):
		return math.pi*self.r*self.r  # 一旦 Circle 定义了自己的 area，从 Shape 继承而来的那个 area 就被重写（overwrite）


class Rectangle(Shape):
	def __init__(self, w=0.0, h=0.0):
		self.w = w
		self.h = h
	# def area(self):
	# 	# return self.w * self.h
	# 	pass
	def area(self):
		return self.w * self.h

if __name__ == '__main__':
	c1 = Circle(10)
	print c1.area()
	rect1 = Rectangle(4,5)
	print rect1.area()
	print Shape.__dict__['area'] # 三个地址不同
	print Circle.__dict__['area']
	print Rectangle.__dict__['area']# 如果Rectangle不重写父类的方法，则地址一致
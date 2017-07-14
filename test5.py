# test5.py
# coding: utf-8
'''
This is Test for vars()
'''
scripts = 'the first line'
pages = 250
lines = 2500
print vars()['scripts']
print vars()['pages']
print vars()['lines']

'''
This is test for callable


'''
def dump(function):
	if callable(function):
		print function, 'it is callable'
	else:
		print function, 'it is NOT callable'

class A:
	def method(self,value):
		return value
class B:
	def __call__(self,value):
		return value

a = A()
b = B()

# dump(B)
# dump(b)
# dump(callable)
# # 1. 类都是默认有__call__函数
# # 2. 实例默认没有__call__函数，除非你自己写
# dump(A.method)
# dump(a.method)

'''
This is test for isinstance(obj, class)
'''
def check_instance(obj,classname):
	if isinstance(obj,classname):
		print obj, ' is instance of ', classname
	else:
		print obj, 'is not instance of', classname

check_instance(a,A)
check_instance(a,B)

'''
检查是否子类
'''

class Shape:
	def __init__(self,width, length):
		self.width = width
		self.length = length
		print 'create a', self
class Round(Shape):
	def __init__(self,radius):
		self.radius = radius
		print 'create a',self
print issubclass(Round,Shape)

'''
学会使用eval(),将表达式换成值
'''
def dump(expression):
	result = eval(expression)
	print expression, '===>', result, type(result)

dump("len('word')")
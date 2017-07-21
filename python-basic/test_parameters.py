# test_parameters.py
# coding: utf-8
'''
1. 必选参数
2. 默认参数
3. 可变参数
4. 关键字参数
'''

def func1(x, y):
	return x+y

def func2(x,y, z=1):
	return x+y+1

def func3(*number): # 这里number其实是一个元组
	result = 0
	for item in number:
		result += item
	return result
def func4(**kwargs):
	result = 0
	for k, v in kwargs.items():
		result += v
	return result


if __name__ == '__main__':
	print func1(3,4)
	print func2(3,4)
	print func3(1,2,3,4,5,6)
	print func4(a=3,b=4,c=5)
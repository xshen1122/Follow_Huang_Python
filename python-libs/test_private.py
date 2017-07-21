# test_private.py
# coding: utf-8
class Foo(object):
	def __init__(self,name):
		self.__name = name

f1 = Foo('fnew')
'''
果然不能调用属性了。__name是私有变量
'''
# print f1.__name
# test_metaclass.py
# coding: utf-8
'''
python的元类是什么鬼？

'''
class Trick(object):
	pass

print type(Trick())
 # 类

# type也可以用来动态创建一个类

print type('Trick', (), {}) # 类
print type('Trick', (), {})() # 对象

# Type实际上是一个元类，用他可以去创建类。什么是元类刚才说了，元类就是创建类的类。也可以说他就是一个类的创建工厂。

'''
元类-黑魔法
略带一点装饰器的思路去理解元类这件事情，可能会让你豁然开朗。
元类这种黑暗魔法按照常理来说是不应该被广泛使用的

'''
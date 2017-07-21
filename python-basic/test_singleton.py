# test_singleton.py
# coding: utf-8
'''
三种方式实现单例模式
1. 什么是单例模式的特点
	1. 每个类只有1个实例
	2. 保证不产生第二个实例
	3. 提供外部对象访问该实例的方法

'''
# 使用__new__
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
 
class Foo(Singleton): #单例类 这个好用的，用Singleton来修饰object
    a = 1
a1 = Foo()
b1 = Foo()
print a1.a, b1.a
print 'a1 is b1:', a1 is b1



# 使用__call__
class Singleton(type):
    def __init__(cls, name, bases, attrs):
        super(Singleton, cls).__init__(name, bases, attrs)
        cls._instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            # 以下不要使用'cls._instance = cls(*args, **kwargs)', 防止死循环,
            # cls的调用行为已经被当前'__call__'协议拦截了
            # 使用super(Singleton, cls).__call__来生成cls的实例
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

class Foo(object): #单例类
    __metaclass__ = Singleton
a = Foo()
b = Foo()
print a is b
a.x = 1
print a.x, b.x # 注意：这里给a实例的x属性赋值为1，b实例的x属性也为1，说明这是a和b共享同一个属性
# 思考：为啥不符合第二点，即不能创建第二个实例？？？


# 使用装饰器
def singleton(cls):
    instances = {}
    def _wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _wrapper
def Person(object):
	pass
a3 = singleton(Person)
b3 = singleton(Person)
print a3 is b3
# 思考：为啥这里a3不等于b3， 两个对象不唯一？
# singleton_2.py
# coding: utf-8
'''
利用__new__

提到__new__就不能不说__init__，先说说关于__new__和__init__的不同与用法：

object.__new__(cls[, ...])：调用创建cls类的一个新的实例。是静态方法不用声明。返回一个新对象的实例

　　　　object.__init__(self[, ...])：当实例创建的时候调用。没有返回值。

__new__在__init__这个之前被调用：

如果__new__返回一个cls的实例，那么新的实例的__init__方法就会被调用，且self是这个新的实例。如果是自定义重写__new__，没有调用__init__的话__init__就不起作用了。

如果__new__不返回一个cls的实例，那么新的实例的__init__方法就不会被调用。

'''
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance
class MyClass1(Singleton):
    a = 1
 

 
one = MyClass1()
two = MyClass1()
 
two.a = 3
print 'one.a=',one.a
'''
OUTPUT:
只需要复制一次，就会改变2个单例的值。（地址相同，指向同样一块内存空间)
one.a= 3
<class '__main__.MyClass1'> 140643032938512
<class '__main__.MyClass1'> 140643032938512


'''
 
assert(isinstance(one,MyClass1))
assert(isinstance(two,MyClass1))
print one.__class__,id(one)
print two.__class__,id(two)
print one == two
print one is two
 
class MyClass2(Singleton):
    a = 2

 
three = MyClass2()
three.a=4
print 'three.a=',three.a
assert(isinstance(three,MyClass2))
print three.__class__,id(three)
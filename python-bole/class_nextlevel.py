# class_nextlevel.py
# coding: utf-8
'''
类的成员可以分为三大类：字段、方法和属性
字段- 静态（属于类）和普通（属于对象）
应用场景： 通过类创建对象时，如果每个对象都具有相同的字段，那么就使用静态字段

方法 - 静态，普通， 类方法
普通方法：以self为输入参数
类方法：用@classmethod修饰，以cls为输入参数
静态方法：用@staticmethod修饰，没有输入参数
后两种都属于类，调用的时候直接用类名修饰； 前者属于对象，调用的时候要被对象修饰

属性- 普通属性

注意：直接从网上贴过来的code可能缩进有问题，不能直接运行
'''
class Province:
	country = 'China' #静态字段属于类，从JAVA处理解，属于类的字段和属于对象的字段存储空间不同

	def __init__(self,province):
		self.province = province

p1 = Province('Hebei')
print p1.province #输出普通字段，即前面要被对象给修饰

print Province.country # 输出静态字段，前面要被类给修饰

class Foo:
	def __init__(self,name):
		self.name = name
	def ord_func(self):
		print 'this is normal func'

	@classmethod
	def class_func(cls):
		print 'this is class func'

	@staticmethod
	def static_func():
		print 'this is static func'

f1 = Foo('Dongdong')
f1.ord_func()
Foo.class_func()
Foo.static_func()

'''
属性存在意义是：访问属性时可以制造出和访问字段完全相同的假象
属性由方法变种而来，如果Python中没有属性，方法完全可以代替其功能
Python的属性的功能是：属性内部进行一系列的逻辑计算，最终将计算结果返回。

使用方法：
    ** 定义时，在普通方法的基础上添加 @property 装饰器；--经典类
    ** 定义时，属性仅有一个self参数
    ** 调用时，无需括号
    方法：foo_obj.func()
    属性：foo_obj.prop

'''
class Foo1:
	def __init__(self,size):
		self.size = size
	@property
	def price(self):
		return 'wupeiqi'

f22= Foo1(5)
print f22.price
# singleton_1.py
# coding: utf-8
'''
1、关于私有方法和属性，我前面已经提到可以用__name形式为名称定义方法名和属性名来解决

2、利用isinstance()或issubclass()

本人力推isinstance()和issubclass()2个方法，正是由于python提供这两个方法才能完成设计模式的开发。

isinstance(object, classinfo)如果object是CLASSINFO的一个实例或是子类，或者如果CLASSINFO和object的类型是对象，或是该类型的对象的子类，返回true。

issubclass(class, classinfo)如果class是CLASSINFO的一个子类返回true。

下面是利用　isinstance实现的Singleton模式


'''
class Singleton:
    __singleton = None
    @classmethod
    def getSingleton(cls):
        if not isinstance(cls.__singleton,cls):
            cls.__singleton = cls()
        return cls.__singleton
 
class Test(Singleton):
    def test(self):
        print self.__class__,id(self)
 
class Test1(Test):
    def test1(self):
        print self.__class__,id(self),'Test1'
 
class Test2(Singleton):
    def test2(self):
        print self.__class__,id(self),'Test2'
 
if __name__=='__main__':
     
 
    t1 = Test.getSingleton()
    t2 = Test.getSingleton()
     
    t1.test()
    t2.test() 
    '''
    OUTPUT:
    __main__.Test 139900075805944
	__main__.Test 139900075805944
	Same!!!
    '''
    assert(isinstance(t1,Test))
    assert(isinstance(t2,Test))
    assert(id(t1)==id(t2))
 
    t1 = Test1.getSingleton()
    t2 = Test1.getSingleton()
 
    assert(isinstance(t1,Test1))
    assert(isinstance(t2,Test1))
    assert(id(t1)==id(t2))
     
    t1.test()
    t1.test1()
    t2.test()
    t2.test1()
    '''
    OUTPUT:
    __main__.Test1 140439424724216
	__main__.Test1 140439424724216 Test1
	__main__.Test1 140439424724216
	__main__.Test1 140439424724216 Test1
	Same!!!!


    '''
 
    t1 = Test2.getSingleton()
    t2 = Test2.getSingleton()
 
    assert(isinstance(t1,Test2))
    assert(isinstance(t2,Test2))
    assert(id(t1)==id(t2))
 
    t1.test2()
    t2.test2()
    '''
    OUTPUT:
    __main__.Test2 139909307559232 Test2
	__main__.Test2 139909307559232 Test2

    '''

    '''

    从运行结果可以看出，我们可以控制同一个子类的生成同一个对象实例，
    但是如果Singleton类被继承（不论是子类之间还是，子类的子类）不能控制生成一个实例。
    这个问题后面再探讨。

    '''
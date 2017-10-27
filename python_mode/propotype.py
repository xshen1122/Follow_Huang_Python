# propotype.py
# coding: utf-8
'''
原型模式：用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。

原型模式与工厂模式一样都生成一个对象，区别就是工厂模式是创建新的对象，
而原型模式是克隆一个已经存在的对象，所以在对象初始化操作比较复杂的情况下，
很实用，它能大大降低耗时，提高性能，因为“不用重新初始化对象，而是动态地获得对象运行时的状态”。

客户（Client）角色：客户类提出创建对象的请求,让一个原型克隆自身从而创建一个新的对象。

抽象原型（Prototype）角色：此角色给出所有的具体原型类所需的接口。

具体原型（Concrete Prototype）角色：被复制的对象。此角色需要实现抽象原型角色所要求的接口。

对于python实现原型模式有现成的copy模块可用。

copy.copy(x)浅拷贝

copy.deepcopy(x) 深拷贝

浅拷贝和深拷贝之间的区别仅适用于复合对象（包含其他对象也就是子对象，如list类或实例对象）：

浅拷贝——构建一个新的对象然后插入到原来的引用上。只拷贝父对象，不会拷贝对象的内部的子对象。

深拷贝——构造一个新的对象以递归的形式，然后插入复制到它原来的对象上。拷贝对象及其子对象Prototype
'''

import copy 
 
class ICloneable: 
    def shallowClone(self): 
        return copy.copy(self) 
      
    def deepClone(self): 
        return copy.deepcopy(self) 
 
class WorkExperience(ICloneable): 
    workData = "" 
    company = "" 
 
class Resume(ICloneable): 
    name = "" 
    sex = "" 
    age = 0 
    work = None 
 
    def __init__(self, name): 
        self.name = name 
        self.work = WorkExperience()
 
    def setPersonInfo(self, sex, age): 
        self.sex = sex 
        self.age = age 
 
    def setWorkExperience(self, workData, company): 
        self.work.workData = workData 
        self.work.company = company
              
    def display(self): 
 
        print('%s, %s, %d' % (self.name,self.sex,self.age)) 
 
        print('%s, %s' % (self.work.workData, self.work.company)) 
 
def client(): 
 
    a = Resume('Tom') 
    a.setPersonInfo('m',29) 
    a.setWorkExperience("1998-2000","ABC.COM")     
 
    b = a.shallowClone()
    b.setWorkExperience("2000-2006","QQ.COM")         
 
    c = a.deepClone()
    c.setWorkExperience("2006-2009","360.COM")     
      
    a.display()
    b.display()   
    c.display()     
    return 
 
if __name__ == '__main__': 
    client();

    '''
    OUTPUT:
    Tom, m, 29
	2000-2006, QQ.COM
	Tom, m, 29
	2000-2006, QQ.COM
	Tom, m, 29
	2006-2009, 360.COM
	a = b 

	从结果可以看出，当b是a的浅拷贝，那么b中的实例对象WorkExperience只会复制了a中的引用，
	当不论是a，b哪一个修改都会改变a和b的WorkExperience实例。

	c是a的深拷贝，创建了新的WorkExperience实例，所以c只会改变自己的WorkExperience

	refer to 
	http://www.uml.org.cn/sjms/201305283.asp
    '''

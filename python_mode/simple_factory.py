# simple_factory.py
# coding:utf-8
'''
专门定义一个类来负责创建其它类的实例，被创建的实例通常都具有共同的父类。
Simple Factory模式不是独立的设计模式，他是Factory Method模式的一种简单的、特殊的实现。
他也被称为静态工厂模式，通常创建者的创建方法被设计为static方便调用，
但是python没有static一说。
所以可以把创建者也就是工厂设计为一个普通class或全局函数即可。
如果是class还需要实例化才能调用工厂方法，而全局函数比较简单，比较接近静态工厂的简便特性。
'''	

class car:

    '''interface as Product'''
    def drive(self):
        pass
 
class BMW(car):
    '''Concrete Product'''
    def __init__(self,carname):
        self.__name=carname
    def drive(self):
        print "Drive the BMW as "+self.__name
 
class Benz(car):
    '''Concrete Product'''
    def __init__(self,carname):
        self.__name=carname
    def drive(self):
        print "Drive the Benz as "+self.__name

#用全局函数改写工厂类        
def driver(name):
	if name=="BMW":
            return BMW("BMW")
        elif name=="Benz":
            return Benz("Benz")
        else:
            raise MyInputException(name)


class driver:
    '''Factory also called Creator'''
    def driverCar(self,name):
        if name=="BMW":
            return BMW("BMW")
        elif name=="Benz":
            return Benz("Benz")
        else:
            raise MyInputException(name)
 
class MyInputException(Exception):  
    def __init__(self, name):  
        Exception.__init__(self)  
        self.name = name
  
 
if __name__ == "__main__":
    print "please input \"BMW\" or \"Benz\" :"
    carname=raw_input()
    dier=driver()
    try:
        d=dier.driverCar(carname)
    except MyInputException,e:
        print "input worry name "+e.name
    else:
        d.drive()
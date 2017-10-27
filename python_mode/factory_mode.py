# factory_mode.py
# coding:utf-8
'''
工厂方法模式去掉了简单工厂模式中工厂方法的静态属性，使得它可以被子类继承。对于python来说，就是工厂类被具体工厂继承。这样在简单工厂模式里集中在工厂方法上的压力可以由工厂方法模式里不同的工厂子类来分担。也就是工厂外面再封装一层。

1) 抽象工厂角色： 这是工厂方法模式的核心，它与应用程序无关。是具体工厂角色必须实现的接口或者必须继承的父类。

2) 具体工厂角色：它含有和具体业务逻辑有关的代码。由应用程序调用以创建对应的具体产品的对象。

3) 抽象产品角色：它是具体产品继承的父类或者是实现的接口。在python中抽象产品一般为父类。

4) 具体产品角色：具体工厂角色所创建的对象就是此角色的实例。由一个具体类实现。

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
 
class driver:
    '''Factory also called Creator'''
    def driverCar(self):
        return car()
 
class BMWdriver(driver):
    '''Concrete Creator'''
    def driverCar(self):
        return BMW("BMW")
 
class Benzdriver(driver):
    '''Concrete Creator'''
    def driverCar(self):
        return Benz("Benz")    
 
if __name__ == "__main__":
    driver=BMWdriver()
    car=driver.driverCar()
    car.drive()
    driver=Benzdriver()
    car=driver.driverCar()
    car.drive()
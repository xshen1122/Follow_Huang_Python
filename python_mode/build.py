# build.py
# coding: utf-8
'''
个人理解，如果说工厂模式旨在选择创建哪一类的实例，而Builder模式的重点是封装一个实例的复杂创建过程。它可以将一个产品的内部表象与产品的生成过程分割开来，从而可以使一个建造过程生成具有不同的内部表象的产品对象。也就是说，建造的步骤可以稳定不变，但是每一步的内部表象可以灵活变化。

1、Builder:为创建Product对象的各个部件指定抽象接口，python中为父类。

2、ConcreteBuilder:实现Builder的接口以构造和装配该产品的各个部件，定义并明确它所创建的表示，并提供一个检索产品的接口，也就是返回产品类的方法。

3、Director:构造一个使用Builer接口的对象，该对象中定义了建造对象的步骤顺序。

4、Product:表示被构造的复杂对象。ConcreteBuilder创建该产品的内部表示并定义它的具体装配方法，包含定义组成部件的类，以及将这些部件装配成最终产品的接口。

一个比较贴切的例子：

要建一座房子，可是我不知道怎么盖，于是我需要找建筑队的工人他们会，还得找个设计师，他知道怎么设计，我还要确保建筑队的工人听设计师的领导，而设计师本身不干活，只下命令，这里砌一堵墙，这里砌一扇门，这样建筑队的工人开始建设，最后，我可以向建筑队的工人要房子了。在这个过程中，设计师是什么也没有，除了他在脑子里的设计和命令，所以要房子也是跟建筑队的工人要。在这个例子中Director是设计师，Builder代表建筑队工人会的建筑技能，ConcreteBuilder工人建筑技能的具体操作，Product就是我要盖的房子。



注：因为python没有private类型的成员，不过我们可以用命名为__name的变量代替，例如上例中的__Room，为什么这样可以呢，我们用builder1=ConcreteBuilder1();print dir(builder1)

打印语句看出如下图，__name实例化后变为__ConcreteBuilder1__name,就是避免外界对__name属性的修改，从而达到了封闭性。


'''
class Builder:
    def BuildWall(self):
        pass
    def BuildDoor(self):
        pass
    def BuildWindow(self):
        pass
    def GetRoom(self):
        pass

class ConcreteBuilder1(Builder):
    def __init__(self):
        self.__Room=[]
    def BuildWall(self):
        self.__Room.append("Builder1 Build the wall. ")
    def BuildDoor(self):
        self.__Room.append("Builder1 Build the door. ")
    def BuildWindow(self):
        self.__Room.append("Builder1 Build the window. ")
    def GetRoom(self):
        return self.__Room

class ConcreteBuilder2(Builder):
    def __init__(self):
        self.__Room=[]
    def BuildWall(self):
        self.__Room.append("Builder2 Build the wall. ")
    def BuildDoor(self):
        self.__Room.append("Builder2 Build the door. ")
    def BuildWindow(self):
        self.__Room.append("Builder2 Build the window. ")
    def GetRoom(self):
        return self.__Room

class Director:
    def __init__(self,Builder):
        self.__build=Builder
    def order(self):
        self.__build.BuildWall()        
        self.__build.BuildWindow()
        self.__build.BuildDoor()
if __name__ == "__main__":
     
    builder1=ConcreteBuilder1()
    director=Director(builder1)
    director.order()
    print builder1.GetRoom()
 
    builder2=ConcreteBuilder2()
    director=Director(builder2)
    director.order()
    print builder2.GetRoom()
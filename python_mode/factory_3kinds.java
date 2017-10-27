// factory_3kinds.java
/*

1. 设计模式的核心是解耦吗？
工厂模式就是为了解耦“需求”和“产品”，但是别忘了，工厂模式工厂模式，还有一个重要元素，
就是“工厂”，所以工厂模式的核心思想，就是解耦“需求”“工厂”和“产品”。


*/
int prodNo;
public SimpleFactory(int prodNo) //构造工厂时告知工厂产品标识
{
    this.prodNo = prodNo;
}

public IProduct GetProduct()
{
    switch (prodNo) //根据产品标识生产产品
    {
        default:
            return new ProductA();
        case 1:
            return new ProductA();
        case 2:
            return new ProductB();
    }

 }


}
//产品A
class ProductA: IProduct 
{
    //产品属性
    //......
}

//产品B
class ProductB : IProduct
{
    //产品属性
    //......
}
//产品接口
interface IProduct
{
    //产品方法
    //......
}
/*
那么大家看看这段简单工厂的例子，如果我现在问，这个会有什么问题，该如何回答呢？
提示一下，如果说来了一个需求，增加一个产品C，该如何办？
没错，简单工厂的问题就在于swich case（或者if else)。
每当新增一种产品时，你都需要去维护工厂中的判断语句，造成的后果就是可能这个工厂类会非常非常长，
各种判断全部挤在一起，给扩展和维护带来很多麻烦。
说白了，你的产品和工厂还是没有完全解耦，绑定在一起的。
所以，我们得到了第二个结论：简单工厂通过构造时传入的标识来生产产品，不同产品都在同一个工厂中生产，
这种判断会随着产品的增加而增加，给扩展和维护带来麻烦。那么，如何解决这个问题呢？ ==> Factory

Function ::  SimpleFactory
Function ::  GetProduct
interface IProduct
class ProductA implements IProduct
class ProductB implements IProduct


*/

interface IFactory //工厂接口
    {
        IProduct GetProduct();
    }
 
//A工厂类
public class FactoryA: IFactory
{
    IProduct productA;
    public FactoryA()
    {
        this.productA = new ProductA();
    }

    public IProduct GetProduct() //A工厂生产A产品
    {
        return this.productA;
    }
}

//B工厂类
public class FactoryB : IFactory
{
    IProduct productB;
    public FactoryB()
    {
        this.productB = new ProductB();
    }

    public IProduct GetProduct() //B工厂生产B产品
    {
        return this.productB;
    }
}

//产品接口
public interface IProduct
{
    //产品方法
    //......
}

//产品A
public class ProductA : IProduct
{
    //产品属性
    //......
}

//产品B
public class ProductB : IProduct
{
    //产品属性
    //......
}
/*
仔细观察这段代码，在工厂模式中，已经将工厂类分开，不再将所有产品在同一工厂中生产，
这样就解决了简单工厂中不停的switch case的问题。
如果说来了一个C产品，那么我们只需要写一个C工厂和C产品，
在调用时用C工厂生产C产品即可，A和B工厂和产品完全不受影响。OK，优化说完了，但是还是有问题。

解耦!解耦!解耦
interface IFactory
interface IProduct
FactoryA implements IFactory
FactoryB implements IFactory
ProductA implements IProduct
ProductB implements IProduct 

===>
FactoryC implements IFacotry
ProductC implements IProduct
*/
/*
问题在哪里呢？当业务需求是需要生产产品族的时候，工厂就不再适合了。
首先我们搞清楚何谓产品族和产品等级结构。
举个例子来说，比如三星是一个品牌，三星生产洗衣机，电视，冰箱；
格力也是一个品牌，格力也生产洗衣机，电视，冰箱。
那么，三星工厂和格力工厂生产的2个品牌的洗衣机，
就在洗衣机这种产品的产品等级结构中
（当然洗衣机产品等级结构中还有LG，海尔，三菱等等不同的品牌的工厂的产品），
所以，洗衣机就是一个产品等级。
那么三星生产的三星洗衣机，三星电视机，三星冰箱就是三星这个工厂的产品族。
可能还会有西门子工厂产品族，格力工厂产品族，美的工厂产品族等等。==> abstract Factory





*/

//工厂接口，即抽象工厂
interface IFactory
{
    IFridge CreateFridge();
    IAirCondition CreateAirCondition();
}


//三星的工厂，生产三星的产品族
public class SamsungFactory : IFactory
{

    public IAirCondition CreateAirCondition() 
    {
        return new SamsungAirCondition(); //三星的工厂生产三星的空调
      
    }

    public IFridge CreateFridge()
    {
        return new SamsungFridge(); //三星的工厂生产三星的冰箱
    }
}

//格力的工厂，生产格力的产品族

public class GreeFactry : IFactory
{
    public IAirCondition CreateAirCondition()
    {
        return new GreeAirCondition(); //格力的工厂生产格力的空调
    }

    public IFridge CreateFridge()
    {
        return new GreeFridge(); //格力的工厂生产格力的冰箱
    }
}

//冰箱产品接口
public interface IFridge
{
    //冰箱产品接口
    //冰箱的action
}

//空调接口
public interface IAirCondition
{
    //空调产品接口
    //空调的action
}

//三星的冰箱
public class SamsungFridge: IFridge
{
   //三星冰箱的action和property
}
//格力的冰箱
public class GreeFridge : IFridge
{
     //格力冰箱的action和property
}

//三星的空调
public class SamsungAirCondition : IAirCondition
{
   //三星空调的action和property
}
//格力的空调
public class GreeAirCondition : IAirCondition
{
    //格力空调的action和property
}

/*
我们可以看到，在工厂模式中，一个工厂生产一个产品，所有的具体产品是由同一个抽象产品派生的，
不存在产品等级结构和产品族的概念；而在抽象工厂中，同一个等级的产品是派生于一个抽象产品（即产品接口）
一个抽象工厂派生不同的具体工厂，每个具体工厂生产自己的产品族（包含不同产品等级）。
所以我们得到第四个结论，工厂模式中，一个工厂生产一个产品，所有产品派生于同一个抽象产品（或产品接口）
而抽象工厂模式中，一个工厂生产多个产品，它们是一个产品族，
不同的产品族的产品派生于不同的抽象产品（或产品接口）。

interface IFactory 
interface IFridge
interface IAirCondition

class SamsungFactory implements IFactory
including SamsungFridge, SamsungAirCondition
class SamsungFridge implements IFridge
class SamsungAirCondition implements IAirCondition

class GreeFactory implements IFactory
including GreeFridge, GreeAirCondition
class GreeFridge implements IFridge
class GreeAirCondition implements IAirCondition




*/
/*
好了我们归纳一下，工厂模式实际上包含了3中设计模式，简单工厂，工厂和抽象工厂，关键点如下：

一、三种工厂的实现是越来越复杂的

二、简单工厂通过构造时传入的标识来生产产品，"不同产品都在同一个工厂中生产"
这种判断会随着产品的增加而增加，给扩展和维护带来麻烦

三、工厂模式无法解决产品族和产品等级结构的问题

四、抽象工厂模式中，一个工厂生产多个产品，它们是一个产品族，
不同的产品族的产品派生于不同的抽象产品（或产品接口）。







*/
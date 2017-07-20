# magic_method.py
# coding: utf-8
'''
1. 实验魔术方法：__init__, __new__, __call__



'''

class Foo(object):
    def __init__(self, *args, **kwargs):
        pass
    def __new__(cls, *args, **kwargs):
        return object.__new__(NotStranger, *args, **kwargs)  
 
class Stranger(object):
	pass

class NotStranger(object):
	pass

 
foo = Foo()
print type(foo)    
 
# 打印的结果显示foo其实是Stranger类的实例。
 
# 因此可以这么描述__new__()和__ini__()的区别，在新式类中__new__()才是真正的实例化方法，为类提供外壳制造出实例框架，然后调用该框架内的构造方法__init__()使其丰满。
# 如果以建房子做比喻，__new__()方法负责开发地皮，打下地基，并将原料存放在工地。而__init__()方法负责从工地取材料建造出地皮开发招标书中规定的大楼，__init__()负责大楼的细节设计，建造，装修使其可交付给客户。


class Word(str):

 
    def __new__(cls, word):
        # 注意我们必须要用到__new__方法，因为str是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')] #单词是第一个空格之前的所有字符
        return str.__new__(cls, word)
 
    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

w1 = Word('Hello')
w2 = Word('Hi')
print w1 > w2
print w1 < w2
print w1 == w2
print w1 >= w2
'''
实验 __str__
'''
class Student(object):
	def __init__(self,name):
		self._name = name
	def __str__(self):
		return 'I am a student: name is ' + self._name # 注意，这里返回值一定是string，不能是元组

s1 = Student('tom')
print s1  # 直接打印不好读，怎么让其显示的更有可读性呢？

'''
实验__iter__
Fib数列，n2=n1+n
'''
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
 
    def __iter__(self):
        return self
 
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a
 
 
for i in Fib():
    print i
'''
实验 __getitem__方法
'''
class MyList(object):
    def __init__(self, *args):
        self.numbers = args
 
    def __getitem__(self, item):
        return self.numbers[item]
 
 
my_list = MyList(1, 2, 3, 4, 6, 5, 3)
print my_list[2]

'''
实验切片功能

'''

class MyList(object):
    def __init__(self, *args):
        self.numbers = args
 
    def __getitem__(self, item):
        if isinstance(item, int):
            return self.numbers[item]
        elif isinstance(item, slice):
            # 写习惯了其他语言，差点忘记了三元运算符的格式了，吼吼吼。
            # 下面句三元运算符的意思是，若为空，则为切片从0开始。
            start = item.start if item.start is not None else 0
            # 下面句三元运算符的意思是，若为空，则为切片到最末端结束。
            stop = item.stop if item.stop is not None else len(self.numbers)
            return self.numbers[start:stop]
 
 
my_list = MyList(1, 2, 3, 4, 6, 5, 3)
print my_list[2:5]
'''
实现切片的负数功能
'''
class MyList(object):
    def __init__(self, *args):
        self.numbers = args
 
    def __getitem__(self, item):
        if isinstance(item, int):
            return self.numbers[item]
        elif isinstance(item, slice):
            start = item.start if item.start is not None else 0
            stop = item.stop if item.stop is not None else len(self.numbers)
 
            length = len(self.numbers)
            start = length + start + 1 if start < 0 else start
            stop = length + stop + 1 if stop < 0 else stop
            return self.numbers[start:stop]
 
my_list = MyList(1, 2, 3, 4, 6, 5, 3)
print my_list[1:-1]

'''
实验__call__方法

'''
class Apple(object):
    def __call__(self, *args, **kwargs):
        return args
 
 
apple = Apple()
print apple("yes", "no")

'''
实验 map方法
'''
def sq(x):
    return x*x  #求x的平方
print map(sq, [1,3, 5,7,9]) #[1, 9, 25, 49, 81]，将list当做x传入
 	
print map(str, [23,43,4545,324]) #['23', '43', '4545', '324']
print map(sq, (1,3, 5,7,9))

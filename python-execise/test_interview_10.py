# test_interview_10.py
# coding: utf-8
'''
十道题
1. 讲下list和tuple的区别
2. 讲下类方法和静态方法的区别
3. list的切片用法
4. 强制转换
5. 编程实现十进制转换为八进制
6. copy和deepcopy的区别
7. lamda的使用
8. with的使用
9. <.*>和<.*?>匹配的区别
10. Set如何使用？

''' 
seq = [1,2,3,4]
def compare(a1,a2):
	if a1==a2:
		print 'correct'
	else:
		print 'wrong'
compare(seq[:2],[1,2]) # 不包含右边所在的2， 只包含0,1

compare(seq[-2:],[3, 4])

compare(seq[10:],[]) #没有元素的list，不是None

compare(seq[::-1],[4,3,2,1])
compare(seq[:],[1,2,3,4])

print id(seq[:])==id(seq) # False, 也就是说seq[:]和seq不是一个instance

# id()函数不多见
'''
Return the “identity” of an object. 
This is an integer (or long integer) which is guaranteed to be unique 
and constant for this object during its lifetime. 
Two objects with non-overlapping lifetimes may have the same id() value.

'''

'''
强制转换：
· int(x)             将x转换为一个整数
· float(x)           将x转换到一个浮点数
· str(x)             将对象 x 转换为字符串
· tuple(s)           将序列 s 转换为一个元组
· list(s)            将序列 s 转换为一个列表
· set(s)             将序列 s 转换为一个集合
   int(x [,base ])         将x转换为一个整数
   long(x [,base ])        将x转换为一个长整数
   float(x )               将x转换到一个浮点数
   complex(real [,imag ])  创建一个复数
   str(x )                 将对象 x 转换为字符串
   repr(x )                将对象 x 转换为表达式字符串
   eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
   tuple(s )               将序列 s 转换为一个元组
   list(s )                将序列 s 转换为一个列表
   chr(x )                 将一个整数转换为一个字符
   unichr(x )              将一个整数转换为Unicode字符
   ord(x )                 将一个字符转换为它的整数值
   hex(x )                 将一个整数转换为一个十六进制字符串
   oct(x )                 将一个整数转换为一个八进制字符串
'''

'''
用算法实现十进制到八进制的转换
提示：
难点在于：多项式的表达
1. 先找到最高阶层的系数
2. 然后用循环法找到次高，。。。。0阶层的系数
3. 将系数放在list
4. 将系数list转换为str，返回str
5. 幂的表达，a**b
'''

s = 100
def my_oct(x):
	xi_list = []
	n=0 # t 是最高幂
	while True:
		if x / 8**n < 8:
			break
		n += 1
	
	xi_list.append(x/(8**n))
	
	
	temp = x
	for i in range(n,0,-1):
		
		temp = temp- xi_list[-1]* 8**i
		
		result = temp/(8**(i-1))
		
		xi_list.append(result)
		
	value = '0'
	for item in xi_list:
		value += str(item)
	return value

print my_oct(10000), type(my_oct(10000))
print oct(10000), type(oct(10000))
	
'''
类方法和静态方法
什么情况下使用静态方法- 普通函数
Python使用静态方法类似函数工具使用，一般尽量少用静态方法
1）静态方法无需传入self参数，类成员方法需传入代表本类的cls参数；
2）从第1条，静态方法是无法访问实例变量的，而类成员方法也同样无法访问实例变量，但可以访问类变量；
3）静态方法有点像函数工具库的作用，而类成员方法则更接近类似Java面向对象概念中的静态方法。
'''


import math
print math.sqrt(10) # 静态方法

'''
copy 和 deepcopy的区别

copy嵌套数组时，copy只copy第一层，第二层是共享的。
deepcopy是完全在内存中区分开
'''
import copy
list1 = [[1,2],[3,4],[5,6],[7,8]]
list2 = copy.copy(list1)
print id(list1[0])
print id(list2[0]) # 指向的元素1的地址一致，说明两者指向同一个元素如果我去修改list1的元素0，那么list2也会改变

#下面看list内指向Obj的情况
list3 = copy.deepcopy(list1)
print id(list3[0]) # 指向的元素1地址变化了，这说明list3完全是一个新的数组


class Dog:
	def __init__(self,name):
		self.name = name
	def __repr__(self):
		return self.name
oudy = Dog('oudy')
candy = Dog('candy')
tom = Dog('tom')
dog_list1 = [oudy,candy,tom]
dog_list2 = copy.copy(dog_list1)
dog_list3 = copy.deepcopy(dog_list1)
print dog_list1[0], dog_list2[0]
oudy.name = 'oudy_new'
dog_list1[0]=oudy
print dog_list1[0], dog_list2[0] # 看到没，只修改了dog_list1 0元素的名字，导致dog_list2 0元素的名字也发生了变化
print dog_list1[0], dog_list3[0] # 此时，dog_list3 0元素的名字不变。。因为它指向单独的存储空间

'''
lambda的用法
lambda用来编写简单的函数，而def用来处理更强大的任务。
一般来讲：lambda就适合编写一行的函数
简单来说，编程中提到的 lambda 表达式，通常是在需要一个函数，
但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数
尤其如果这个函数只会使用一次的话。而且第一种写法实际上更易读，
因为那个映射到列表上的函数具体是要做什么，非常一目了然。
如果你仔细观察自己的代码，会发现这种场景其实很常见：
你在某处就真的只需要一个能做一件事情的函数而已，连它叫什么名字都无关紧要。
Lambda 表达式就可以用来做这件事。

这样的写法时，你会发现自己如果能将「遍历列表，
给遇到的每个元素都做某种运算」的过程从一个循环里抽象出来成为一个函数 map，
然后用 lambda 表达式将这种运算作为参数传给 map 的话，考虑事情的思维层级会高出一些来，
需要顾及的细节也少了一点。

这种能够接受一个函数作为参数的函数叫做「高阶函数」（higher-order function）

'''
f = lambda x,y,z : x+y+z
print f(1,2,3)
print map(lambda x: x*x ,[y for y in range(10)]) # 此时lambda函数为乘方函数

'''
with语句， 上下文管理

with最多的 就是打开文件，和实现__enter__和__exit__
个人理解with常用在try-except-finally,需要在finally对资源进行释放类型的模型

使用with语法可以使用上下文管理器，实现上下文协议__enter__和__exit__，在__exit__中队资源进行释放

此时打开某个文件，不需要记住关闭文件（释放资源）
'''

with open(r'somefileName') as somefile:
    for line in somefile:
        print line
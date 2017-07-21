# test_tips.py
# coding: utf-8
'''
python编程的30个tips

'''
#转换
x, y = 10, 20
print(x, y)
 
x, y = y, x # 直接用这个能完成转换，之前C需要temp的中间变量完成x，y的值互换
print(x, y)

#链状比较符

n = 10
result = 1 < n < 20
print(result)
  
result = 1 > n <= 9
print(result)

# 使用三元赋值
def small(a, b, c):
    return a if a <= b and a <= c else (b if b <= a and b <= c else c)
 
print(small(1, 0, 1))
print(small(1, 2, 2))
print(small(2, 2, 3))
print(small(5, 4, 3))

# 将list的值赋给变量
testList = [1,2,3]
x, y, z = testList
 
print(x, y, z)

# 打印引进模块的绝对路径
import pdir 
import socket
 
print(pdir)
print(socket)

# 字典集合的推导，非常简洁
testDict = {i: i * i for i in xrange(10)} 
testSet = {i * 2 for i in xrange(10)}
 
print(testSet)
print(testDict)

# 拼接字符串
test = ['I', 'Like', 'Python', 'automation']
print ' '.join(test)
print str.join(' ',test) # 第一个参数是str，第二个参数是list

#翻转列表本身
testList = [1, 3, 5]
testList.reverse()
print(testList)

# 在循环中翻转
for element in reversed([1,3,5]):
    print(element)

# 玩转枚举
testlist = [10, 20, 30]
for i, value in enumerate(testlist):  #可以同时获得下标和值
    print(i, ': ', value)

# 在python中使用枚举量
class Shapes:
    Circle, Square, Triangle, Quadrangle = range(4)
 
print(Shapes.Circle)
print(Shapes.Square)
print(Shapes.Triangle)
print(Shapes.Quadrangle)


#在方法中返回多个值 ， 好用啊
# function returning multiple values.
def x():
    return 1, 2, 3, 4
 
# Calling the above function.
a, b, c, d = x()
 
print(a, b, c, d)

# 在函数参数中使用运算符
def test(x, y, z):
    print(x, y, z)
 
testDict = {'x': 1, 'y': 2, 'z': 3} 
testList = [10, 20, 30]
 
test(*testDict)
test(**testDict)
test(*testList)

# 找出最频繁出现的数， 好用啊。
test = [1,2,3,4,2,2,3,1,4,4,4]
print(max(set(test), key=test.count))

#两个相关list构建一个字典， 好用啊。
t1 = (1, 2, 3)
t2 = (10, 20, 30)
 
print(dict (zip(t1,t2)))
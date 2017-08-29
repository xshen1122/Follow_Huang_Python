# sixteen_problems.py
# coding: utf-8
'''
def print_directory_contents(sPath):
    """
    这个函数接受文件夹的名称作为输入参数，
    返回该文件夹中文件的路径，
    以及其包含文件夹中文件的路径。

    """
    # 补充代码

'''
import os
# def print_directory_contents(sPath):
# 	return os.walk(sPath)
def print_directory_contents(sPath):
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath) #闭包函数
        else:
            print sChildPath



'''
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))- 字典 {'a':1,'b':2,'c':3,'d':4,'e':5}
A1 = range(10) - 数组 0,1,2,3,4...9
A2 = [i for i in A1 if i in A0]- 数组 - 找出A1和A0的子集， 1,2,3,4,5?
A3 = [A0[s] for s in A0] - 数组- 1,2,3,4,5
A4 = [i for i in A1 if i in A3]- 1,2,3,4,5
A5 = {i:i*i for i in A1}  - 字典：0,1,4,9.。。。
A6 = [[i,i*i] for i in A1] - 数组：[[0,0],[1,1],[2,4]...]

'''
def test2():
	A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
	print A0
	A1 = range(10)
	print A1
	A2 = [i for i in A1 if i in A0]
	print A2 #为啥是[]
	A3 = [A0[s] for s in A0]
	print A3
	A4 = [i for i in A1 if i in A3]
	print A4
	A5 = {i:i*i for i in A1}
	print A5
	A6 = [[i,i*i] for i in A1]
	print A6
	for i in A0:
		print i #取出的是key
'''
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print l


'''
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print l

class A(object):
    def go(self):
        print "go A go!"
    def stop(self):
        print "stop A stop!"
    def pause(self):
        raise Exception("Not Implemented")
class B(A):
    def go(self):
        super(B, self).go() # 先调用父类的go
        print "go B go!" # 再定义自己的go

class C(A):
    def go(self):
        super(C, self).go()
        print "go C go!"
    def stop(self):
        super(C, self).stop()
        print "stop C stop!"

class D(B,C):
    def go(self):
        super(D, self).go()
        print "go D go!"
    def stop(self):
        super(D, self).stop()
        print "stop D stop!"
    def pause(self):
        print "wait D wait!"

class E(B,C): pass




if __name__ == '__main__':
	# print_directory_contents(r'C:\Users\real-qa\_0418')
	# test2()
	# f(2) # [0,1]
	# f(3,[3,2,1]) # [3,2,1,0,1,4]
	# f(3) # [0,1,4]
	# f(4)
	# f(7) # 它使用了之前内存地址中存储的旧列表。这就是为什么它的前两个元素是0和1了。
	a = A()
	b = B()
	c = C()
	d = D()
	e = E()
	print 'a.go()', a.go() # go A go!
	

	print 'b.go()', b.go() # b 继承了A类的go函数，并构建了自己的go函数

	print 'c.go()', c.go() # c 继承了A类的go函数，并构建了自己的go函数

	print 'd.go()', d.go() # 同时继承了c，b，a，并构建了自己的go函数

	print 'e.go()', e.go() # 同时继承了c，b，a，没有构建自己的go函数


	print 'a.stop()', a.stop()
	print 'b.stop()', b.stop()
	print 'c.stop()', c.stop()
	print 'd.stop()', d.stop()
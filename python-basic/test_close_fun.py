# test_close_fun.py
# coding: utf-8
'''
直接def f1 ， f2 是不行的
思考：怎么把f1弄成和make_printer类似？不能打印出数字2啊？？？
思路：可以在f2函数中给变量起新的名字。。。不能写成n = n +1 
'''

def f1(n):
	
	def f2():
		# n = n +1 # 不能使用n=n+1????，但给变量起个新名字，就没问题了。。
		n1 = n+1
		print n1
	return f2

def make_printer(msg):
    def printer():
        print msg + 'hello'  # 夹带私货（外部变量）
    return printer  # 返回的是函数，带私货的函数
 
printer = make_printer('Foo!')
printer()

f2 = f1(1)
f2()
# 以上两个函数只能把f1 的传参原封不动的输出
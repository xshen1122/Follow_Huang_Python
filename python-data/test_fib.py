# test_fib.py
# coding: utf-8
'''
递归是理解树的前提。
递归 - fib数列

'''
def fib(n):
	if n==1 or n==2:
		return 1
	else:
		return fib(n-1) + fib(n-2) #这里就用到了递归思想，就是函数自己调用自己

for i in range(1,10):
	print fib(i)

'''
树借助规模更小的子树来定义

'''
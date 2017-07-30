# test_generator.py
# coding: utf-8
'''
Generator: 

    可迭代对象(Iterable)
    迭代器(Iterator)
    迭代(Iteration)
Python中任意的对象，只要它定义了可以返回一个迭代器的__iter__方法，
或者定义了可以支持下标索引的__getitem__方法)，那么它就是一个可迭代对象。

任意对象，只要定义了next(Python2) 或者__next__方法，它就是一个迭代器

用简单的话讲，它就是从某个地方（比如一个列表）取出一个元素的过程。
当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代。

best usage
这个案例并不是非常实用。生成器最佳应用场景是：
你不想同一时间将所有计算出来的大量结果集分配到内存当中，
特别是结果集里还包含循环。
'''

def generator_func():
	for i in range(10):
		yield i


def fib(n):
	a = b = 1
	for i in range(n):
		yield a
		a, b = b, a+b 
if __name__ == '__main__':
	f = fib(10)
	# while True:
	# 	try:
	# 		print f.next()
	# 	except Exception, e:
	# 		raise e
	# 		break
	my_string = "Yasoob"
	my_iter = iter(my_string)
	print next(my_iter)
	print next(my_iter)
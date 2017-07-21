# test_queue.py
# coding: utf-8
'''
队列（queue），是先进先出（FIFO, First-In-First-Out）的线性表，
在具体应用中通常用链表或者数组来实现，队列只允许在后端（称为rear）进行插入操作，
在前端（称为front）进行删除操作，队列的操作方式和堆栈类似，唯一的区别在于队列只允许新数据在后端进行添加


collections的queue是单向队列
Queue()        定义一个空队列，无参数，返回值是空队列。
enqueue(item)  在队列尾部加入一个数据项，参数是数据项，无返回值。
dequeue()      删除队列头部的数据项，不需要参数，返回值是被删除的数据，队列本身有变化。
isEmpty()      检测队列是否为空。无参数，返回布尔值。
size()         返回队列数据项的数量。无参数，返回一个整数。


要自己实现Queue

四种数据结构，列表，Stack，队列，链表
python中只有Stack和deque，没有链表。为什么没有链表？
如果你要用它来做其他事情，可以看看有没有你需要的第三方模块,
或者可以用C来实现自己的一个模块，python本来就是C写的，所以这实际上也一点不困难。
比如python里面没有一个数据结构是能用来很好表示数值运算中使用的大型矩阵或者数组的，这时候就诞生了第三方包：numpy
'''
# from collections import queue
class Queue:
	def __init__(self):
		self.items = []  # 定义列表
	def isEmpty(self):
		return self.items == []
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeue(self):
		self.items.pop() # 只操作，没有返回值
	def size(self):
		return len(self.items)

q1 = Queue()
q1.enqueue('a')
q1.enqueue('b')
q1.enqueue('c')

print q1.dequeue(), q1.size()
print q1.dequeue(), q1.size()
print q1.dequeue(), q1.size()
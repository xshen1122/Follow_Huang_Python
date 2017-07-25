# test_node.py
# coding: utf-8
'''
list的扩展，链式存储结构
1. 网友各自的实现不同，但是把nextp设置为0不合适。
2. 第二种方法

'''
'''
class Node(object):
	def __init__(self,data,nextp=0):
		self.data = data
		self.nextp = nextp
# 先定义Node，数据结构， 在定义LinkedList
class LinkedList(object):
	def __init__(self,head):
		self.head=0

这种定义不合理
'''
'''
下面这种比较合理。
注意：Node数据结构和LinkedList没有直接关系。
两个难点：先有Node结构，再有LinkedList结构， 弄一个可移动的指针 pre

"核心： 工作指针后移"

Node：有两个数据，一个是data，一个是指向下一个Node对象
LinkedList：只有self.head, pre=self.head是中间变量。
要完成的方法列表
__len__:返回链表的长度

__getitem__:返回某个位置上的量，返回的是data

insert(index, obj):在某个位置上插入, 还是老办法，移动指针到指定位置上，将pre.nextp 指向新加的数据，并用temp
保存index之后的数据，最后将新加入的Node的nextp指向temp

以上为单向链表

还有其他链表形式:
1. 静态链表
2. 循环链表
将Tail的指针指向Head
3. 双向链表
用空间来换取时间


'''
class Node(object):
	def __init__(self,data):
		self.data = data
		self.nextp = None # 注意nextp不能作为私有，因为LinkedList还需要调用。

class LinkedList(object):
	# python的类不支持多个__init__,通过默认参数或者可变参数来实现__init__的多态
	def __init__(self,list1=[]):
		self.head = None
		if list1 != []:
			for data in list1:
				self.append(data)

	def __str__(self):
		pre = self.head # 这里不对self.head直接操作是有理由的，不然self.head就挪位置了
		result = str(pre.data) 
		
		
		while pre.nextp:
			result = result +  ' , ' + str(pre.nextp.data) 
			pre= pre.nextp  # 指向下一个Node
		return result
	def clear(self):
		self.head = None

	def insert(self,index, data):
		pre = self.head
		for i in range(index-1):
			pre = pre.nextp
		temp = pre.nextp
		node = Node(data)
		pre.nextp = node
		pre = pre.nextp
		pre.nextp = temp

    	

	def __getitem__(self,index):
		if self.head == None:
			return 'LinkedList is empty'
		pre = self.head
		for i in range(index):
			pre = pre.nextp
		return pre.data
		


	def __len__(self):
		size = 0
		pre = self.head # 保持self.head 不动。pre作为可移动的指针
		if pre == None:
			return 0
		else:
			while pre.nextp:

				size += 1
				pre = pre.nextp
		return size + 1

	def append(self,data):

	    node=Node(data)

	    if self.head == None:
	    	self.head = node
	    else:
	    	pre = self.head

	    	while pre.nextp:
	    		pre = pre.nextp
	    	pre.nextp = node


    

if __name__ == '__main__':
	llist = LinkedList()
	llist.append('a')
	llist.append('b')
	llist.append('c')

	llist.append('d')

	llist.insert(1,'e')
	print str(llist)


	list1 = [1,2,3,4]
	llist1 = LinkedList(list1)
	print str(llist1)

	llist1.clear()
	print len(llist1)




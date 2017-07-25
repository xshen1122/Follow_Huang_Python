# test_1.py
# coding: utf-8
'''
已知一个由纯数字(顺序由小按大排序)元素组成的列表，比如

li=[1,2,3,4,5,7,8,15,20,21,22,23,24,28]

写一个函数，让它返回如下的字符串

str='1~5,7~8,15,20~24,28'

若数字连续，中间部分用 ~ 省略。

思路
1. 遍历数组，先找出连续的一组数，然后存在str1里面
2. 继续找
放在队列里？
3. 最后一个28的处理有讲究
'''
class Queue:
	def __init__(self,yourlist):
		yourlist.reverse()
		self.items = yourlist  # 定义列表
	def isEmpty(self):
		return self.items == []
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeue(self):
		self.items.pop() # 只操作，没有返回值
	def size(self):
		return len(self.items)
	def __getitem__(self,index):
		return self.items[index]

if __name__ == '__main__':
	yourlist = [1,2,3,4,5,7,8,15,20,21,22,23,24,28,29,30,31,100]
	queue = Queue(yourlist)
	start = queue[-1]
	temp = queue[-1]
	flag = False
	last_two = 0
	while queue.size()!=1:
		last_two = queue[-1]
		queue.dequeue()
		
		if queue[-1] - temp != 1:
			end = temp
			if start == end:
				print str(start)
			else:
				print str(start) + '~' + str(end)
			start = queue[-1]

		




		temp = queue[-1]

	last_one = queue[-1]
	
	# print 'last_one',last_one
	# print 'last_two', last_two  # 非常有必要把倒数第二个记下来,因为需要特别处理最后一个元素
	if last_one - last_two == 1:
		print str(start) + '~' + str(last_one)
	else:
		print str(start)

	
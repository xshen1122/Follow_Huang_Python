# test_stack_1.py
# coding: utf-8
'''
跟着大话数据结构 - 学栈和队列

栈 - 只允许在栈顶进行插入和删除pop- 弹出，从栈内删除
队列 - 在一端插入，另外一端删除

python里有弄好的stack
'''

class Stack:
	def __init__(self):
		self.items = []
	def push(self,data):
		self.items.append(data)
	def pop(self):
		self.items.pop()
	def __len__(self):
		return len(self.items)
	def __getitem__(self,index):
		return self.items[index]
'''
用栈实现Fib
前面相邻两个相加得到该数
用递归法实现Fib
'''
def Fib(k):
	if k==1 or k==2:
		return 1
	else:
		return Fib(k-1) + Fib(k-2)

		 





if __name__ == '__main__':
	# s1 = Stack()
	# s1.add(1)
	# s1.add(2)
	# print s1[-1]
	# s1.pop()
	# print s1[-1]

	
	s1 = Stack()
	for i in range(1,10):
		s1.push(Fib(i))
	result = ''
	for item in s1:
		result = result + '  ' + str(item)
	print result

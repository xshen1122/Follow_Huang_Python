# test_4.py
# coding: utf-8
'''
从终端读入一个整数n，随机一个输入一个0 或1 判断连续是0 或1 的最大次数。如： 
输入 0 0 0 1 1 1 1 0 1 0 1在连续输入中，出现4次
利用之前分解数组的知识。。。
'''
class Stack:
	def __init__(self,yourstring):
		self.items = []
		for item in yourstring:
			self.items.append(item)
		self.items.reverse()
	def push(self,data):
		self.items.append(data)
	def pop(self):
		self.items.pop()
	def onTop(self):
		return self.items[-1]
	def __len__(self):
		return len(self.items)
	def __getitem__(self,index):
		return self.items[index]


def max_count(yourstring):
	s1 = Stack(yourstring)
	print s1.items
	temp = 0
	maxcount = 0
	start = s1.onTop()
	print start
	while len(s1) > 1:
		s1.pop()
		if s1.onTop() == start:
			temp += 1
		else:
			start = s1.onTop()
			print 'temp', temp
			if temp>maxcount:
				maxcount = temp
	return maxcount
# test13.py
# coding: utf-8
'''
比如列表[0,0,0,1,1,2,3,3,3,2,3,3,0,0]分割成[0,0,0],[1,1],[2],[3,3,3],[2],[3,3],[0,0]

'''

'''
思路：
1. 取出第一组相同元素，返回相同元素组成的数组，和pos
2. 去掉第一组元素，从pos开始 yourlist[pos:]
3. 循环取出第一组相同元素，直到len(yourlist)>1 (还有数组)

'''
def parse_list(yourlist):
	result_list = []
	def get_first_list(yourlist):
		new_list = []
		
		for i in range(0,len(yourlist)):
			
			if yourlist[i] == yourlist[0]:
				new_list.append(yourlist[i])
			else:
				return new_list, i
		return new_list,i
	pos=1
	while not pos==0:
		result,pos= get_first_list(yourlist)
		result_list.append(result)
		
		yourlist = yourlist[pos:]

	if result_list[-1]==[0]:
		return result_list[:-1]
	else:
		return result_list
	
'''
最后连续2个相同元素的还需要再调下。思路不太清楚了。
'''


def test_parse_list():
	yourlist = [0,0,0,1,1,2,3,3,3,2,3,3,0,0,5]
	max_count = 0
	

def get_max_count(yourlist):
	max_count = 0
	for item in parse_list(yourlist):
		if len(item) > max_count:
			max_count = len(item)
	print 'max_count is ', max_count

if __name__ == '__main__':
	print 'Give your 01 string'
	str1 = raw_input()
	yourlist = []
	for item in str1:
		yourlist.append(item)
	get_max_count(yourlist)


	


# if __name__ == '__main__':
# 	
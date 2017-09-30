# test_xiaobai_11.py
# coding: utf-8
import copy
'''


In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
20x20的网格，比较有意思。（横线，竖线，对角线的4个数的乘积最大）
这道题考验数据结构了，怎么把20x20的矩阵表示为好用的数据结构
思路：
 定义一个Grid类，完成以下功能
1. 从grid.txt获取grid列表，这里的难点在于将20x20的网格变化为一个二维列表
2. 横方向的四个乘积比较好算f[n]*f[n+1]*f[n+2]*f[n+3], n 从0开始，一直到n+3 = len（f）-1， n=len（f）-4

其他考虑点
横方向的line，colomn存储还没完全想好
竖方向的可以先将矩阵倒置后（line，colomn互换，直接调用横方向的函数）
斜方向的也不简单。需要配成多个list(（难点在于每个list的长度不同）)

如果想保留原来的矩阵，需要用copy.deepcopy(list1),否则直接赋值是无法保留原来的值。(也会更新到新的矩阵）


'''
class Grid():
	def __init__(self,filename):
		self.filename = filename
		self.grid_whole_list = []
		self.origin_grid_whole_list = []
	def getGridList(self):

		myfile = open(self.filename,'r')
		grid_list = []
		grid_number_list = []
		
		for line in myfile.readlines():
			grid_list.append(line.split())
		for i in range(len(grid_list)-1):

			grid_number_list=[]
			for j in range(len(grid_list[i])-1):
				
				grid_number_list.append(int(grid_list[i][j]))
			self.grid_whole_list.append(grid_number_list)
		self.origin_grid_whole_list = copy.deepcopy(self.grid_whole_list)
	def getVGridList(self):
		

		for i in range(len(self.grid_whole_list)):
			for j in range(i+1, len(self.grid_whole_list)):
				temp=self.grid_whole_list[i][j]
				self.grid_whole_list[i][j]=self.grid_whole_list[j][i]
				self.grid_whole_list[j][i]=temp
		
	def getDiagGridList(self):
		


	def checkHorizon(self):
		line_dict = {}
		for line in range(len(self.grid_whole_list)):
			grid_dict={}
			whole_list=[]
			item = self.grid_whole_list[line]
			for n in range(0,len(item)-3):
				grid_dict.setdefault(n,item[n]*item[n+1]*item[n+2]*item[n+3])
			# print '------------------------------------------------------'
			# print line
			raw = sorted(grid_dict.items(),key=lambda d: d[1],reverse=True)[0][0]
			# print raw
			value = sorted(grid_dict.items(),key=lambda d: d[1],reverse=True)[0][1]
			# print value


			 
			line_dict.setdefault(line,[raw, value])
		# print line_dict	
		# print sorted(line_dict.items(),key=lambda d: d[1][1],reverse=True)
		return sorted(line_dict.items(),key=lambda d: d[1][1],reverse=True)[0]
		'''
		哈哈，做出来了，把行和列的信息都存在字典里。
		字典的value可以放一个list
		最后算出横向最大的数为(8,[10,48477312])，就是第8行（从0开始），第10列（从0开始）
		'''

	def checkVertical(self):
		
		self.getVGridList()
		
		ss = self.checkHorizon()
		return ss


	def checkDiagonal(self):
		pass
	def process(self):
		self.getGridList()
		print self.checkHorizon()
		print '-----over-----'
		print self.checkVertical()

		self.checkDiagonal()



if __name__ == '__main__':
	test = Grid('grid.txt')
	test.process()
	print test.origin_grid_whole_list
	print test.grid_whole_list
	print 66*91*88*97
	
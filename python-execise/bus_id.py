# bus_id.py
# coding:utf-8
'''
bus的灯牌打印
*   ***
*     *
*   ***
*   *
*   ***

5x5 matrix, 3x5 not empty, 2x5- space
这里比较后的使用了--字典完成函数映射
可以通过switcher来传递参数
	def printNumber(self,n,offset):
		switcher={0:self.printZero,1:self.printOne,2:self.printTwo,3:self.printThree,4:self.printFour,5:self.printFive, 
		          6:self.printSix, 7:self.printSeven, 8:self.printEight, 9:self.printNine}
		func = switcher.get(n,lambda: 'nothing')
		
		return func(offset)	
3 Points:
1. 给定函数名字，self.printOne（在类中）, 或者printOne（在类外）
2. 通过一个命令来指定函数： func = switcher.get(n,lambda: 'nothing')
3. 传递参数， func(offset)


'''
class BusLight:
	def __init__(self,number):
		self.number=number
		self.position=[]
		for i in range(len(str(number))):
			self.position.append((int(str(number)[i]),i))

		self.total_list=[]

	def printFrame(self):
		#current it's 3 digits:
		
		
		for line in range(5):
			str_list=[]
			for row in range(15):
				str_list.append(' ')
			self.total_list.append(str_list)

	

	

	def covertListToStr(self):
		str1=''
		for item in self.total_list:
			for jtem in item:
				str1 += jtem
			str1 += '\n'
		print('\033[1;31;40m')
		print str1

	def printNumber(self,n,offset):
		switcher={0:self.printZero,1:self.printOne,2:self.printTwo,3:self.printThree,4:self.printFour,5:self.printFive, 
		          6:self.printSix, 7:self.printSeven, 8:self.printEight, 9:self.printNine}
		func = switcher.get(n,lambda: 'nothing')
		
		return func(offset)		
		
	def printLight(self):
		self.printFrame()
		for item in self.position:
			
			self.printNumber(item[0],item[1])


	def printZero(self,offset):
		print 'zero'
		str1 = ''
		for line in range(5):
			for row in range(0+5*offset,5+5*offset):
				if line==0 and row!=4+5*offset or line==4 and row!=4+5*offset or row==0+5*offset or row==3+5*offset:
					self.total_list[line][row]='*'
			
		
	

	def printOne(self,offset):
		print 'call printOne'
		
		
		for line in range(5):
			for row in range(0+5*offset,5+5*offset):
				if row==1+5*offset:
					self.total_list[line][row]='*'


	

	def printTwo(self,offset):
		print 'call printTwo'
		for line in range(5):
			for row in range(0+5*offset,5+5*offset):
				if line == 0 and row!=4+5*offset or line==2 and row!=4+5*offset or line==4 and row!=4+5*offset or line==1 and row==3+5*offset or line==3 and row==0+5*offset:
					self.total_list[line][row]='*'

	def printThree(self,offset):
		print 'call printThree'
		for line in range(5):
			for row in range(0+5*offset,5+5*offset):
				if line == 0 and row!=4+5*offset or line==2 and row!=4+5*offset or line==4 and row!=4+5*offset or line==1 and row==3+5*offset or line==3 and row==3+5*offset:
					self.total_list[line][row]='*'

	def printFour(self,offset):
		print 'call printFour'
		for line in range(5):
			for row in range(0+5*offset,5+5*offset):
				if line==2 and row!=4+5*offset or row==3+5*offset or row==0+5*offset and line not in [2,3,4]:
					self.total_list[line][row]='*'

	def printFive(self,offset):
		print 'call printFive'

		for line in range(5):
			for row in range(0+5*offset,5+5*offset):
				if line == 0 and row!=4+5*offset or line==2 and row!=4+5*offset or line==4 and row!=4+5*offset or line==1 and row==0+5*offset or line==3 and row==3+5*offset:
					self.total_list[line][row]='*'
	def printSix(self,offset):
		print 'call printSix'
		for line in range(5):
			for row in range(0+5*offset,5+5*offset):
				if line == 0 and row!=4+5*offset or line==2 and row!=4+5*offset or line==4 and row!=4+5*offset or line==1 and row==0+5*offset or line==3 and row==3+5*offset or row==0+5*offset:
					self.total_list[line][row]='*'


	def printSeven(self,offset):
		print 'call printSeven'
		for line in range(5):
			for row in range(0+5*offset,5+5*offset):
				if line==0 and row!=4+5*offset or row==3+5*offset:
					self.total_list[line][row]='*'
	def printEight(self,offset):
		print 'call printEight'
		for line in range(5):
			for row in range(0+5*offset,5+5*offset):
				if line == 0 and row!=4+5*offset or line==2 and row!=4+5*offset or line==4 and row!=4+5*offset or line==1 and row==0+5*offset or row==3+5*offset or line==3 and row==3+5*offset or row==0+5*offset:
					self.total_list[line][row]='*'

	def printNine(self,offset):
		print 'call printNine'
		for line in range(5):
			for row in range(0+5*offset,5+5*offset):
				if line == 0 and row!=4+5*offset or line==2 and row!=4+5*offset or line==4 and row!=4+5*offset or line==1 and row==0+5*offset or row==3+5*offset or line==3 and row==3+5*offset :
					self.total_list[line][row]='*'


	# 完成函数的映射

if __name__ == '__main__':
	# print printNumber(1,0)
	test_list=[110,16,717,606,592,119,110,484,333,300,616,432,392,393,692]
	for item in test_list:
		test = BusLight(item)
		print test.position
		test.printLight()
		test.covertListToStr()
	# test.printOne(0)
	# test.printOne(1)
	# test.printZero(2)
	# test.covertListToStr()

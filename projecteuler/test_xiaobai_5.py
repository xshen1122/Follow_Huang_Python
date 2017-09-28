# test_xiaobai_5.py
# coding: utf-8
'''


2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by 
all of the numbers from 1 to 20?

Good idea:
所有质数相乘2*3*5*7*11*13*17*19=9699690,
所有合数4 6 8 9 10 12 14 15 16 18 20,
分解质因数16有4个2,9有两个3,5*5=25＞20,
所以大于5的质因数在20以内的合数中至多有一个,
所以9699690在补上3个2,1个3即9699690*2*2*2*3=232792560


'''
def checkNumber(number):
	flag=True
	for item in range(2,20):
		if number%item == 0:
			flag=flag*True
		else:
			return False
	return True
if __name__ == '__main__':
	i=332792560
	while True:
		if checkNumber(i):
			print 'smallest positive number is ', i 
			break
		i -= 1
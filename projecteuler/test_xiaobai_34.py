# test_xiaobai_34.py
# coding: utf-8
'''


145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.



'''
def Mi(number):
	result = 1
	for i in range(1,number+1):
		result *= i
	return result
def checkMi(number):
	number_list = []
	result = 0
	for item in str(number):
		number_list.append(int(item))
	for item in number_list:
		result += Mi(item)
	if number == result:
		return True
	else:
		return False
if __name__ == '__main__':
	for i in range(14,100000000):
		if checkMi(i):
			print i
	
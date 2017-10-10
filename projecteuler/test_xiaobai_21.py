# test_xiaobai_21.py
# coding: utf-8
'''


Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.


'''
def getDivisor(number):
	divisor_list = []
	result = 0
	for i in range(1,number):
		if number%i == 0:
			divisor_list.append(i)
	for item in divisor_list:
		result += item
	return result

if __name__ == '__main__':
	existing_list=[]
	for number in range(10,10001):
		newone = getDivisor(number)

		if getDivisor(newone) == number and newone != number and number not in existing_list and newone not in existing_list:
			print number, newone, 'are amicable numbers'
			existing_list.append(number)
			existing_list.append(newone)
'''
最后加的判断条件是用来去掉：
1. number的重复项
2. number和newnumber互为一对的重复项。比如220和284,284和220

'''
'''
OUTPUT:
220 284 are amicable numbers
1184 1210 are amicable numbers
2620 2924 are amicable numbers
5020 5564 are amicable numbers
6232 6368 are amicable numbers


'''
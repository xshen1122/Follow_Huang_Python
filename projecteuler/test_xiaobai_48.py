# test_xiaobai_48.py
# coding: utf-8
'''


The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.


'''
def myPow(x,y):
	result = 1
	for i in range(y):
		result *= x
	return result

if __name__ == '__main__':
	total = 0
	for number in range(1,1001):
		total += myPow(number,number)
	print total
	print str(total)[-11:-1]

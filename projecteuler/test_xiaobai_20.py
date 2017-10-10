# test_xiaobai_20.py
# coding: utf-8
'''


n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


'''
from test_xiaobai_16 import *
def jieCheng(number):
	result =1 
	for i in range(1,number+1):
		result *= i
	return result
print jieCheng(100)
print getSum(jieCheng(100))

# answer is 648, we can use test_xiaobai_16 common function getSum(number)
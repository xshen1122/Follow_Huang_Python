# test_xiaobai_10.py
# coding: utf-8
'''


The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.2000000

'''
from test_xiaobai_7 import *

def findZhiNumber(number):
	sum_value=0
	for i in range(2,number):
		if checkZhiNumber(i):
			sum_value += i
	return sum_value

if __name__ == '__main__':
	findZhiNumber(2000000)
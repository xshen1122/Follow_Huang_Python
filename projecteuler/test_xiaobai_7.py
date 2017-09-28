# test_xiaobai_7.py
# coding: utf-8
'''


By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

这道题比较考验电脑速度，用python跑一分钟才能求得第10001个质数

'''
def checkZhiNumber(number):
	for i in range(2,number):
		if number%i == 0:
			return False
	return True
number = 2
zhi_list = []
while len(zhi_list)<10001:
	if checkZhiNumber(number):
		zhi_list.append(number)
	number += 1

print '10001st prime number is ' , zhi_list[-1]
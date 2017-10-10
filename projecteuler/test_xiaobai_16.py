# test_xiaobai_16.py
# coding: utf-8
'''


215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?


'''
import math

def myPow(number):
	result = 1
	for i in range(number):
		result *= 2
	return result

def getMiSum(number):
	
	your_digit = myPow(number)
	your_string = str(your_digit)
	result = 0
	for item in your_string:
		result += int(item)
	
	return result
def getSum(number):
	your_string = str(number)
	result = 0
	for item in your_string:
		result += int(item)
	return result
def getMathSum(number):
	your_digit = int(math.pow(2,number))
	your_string = str(your_digit)
	result = 0
	for item in your_string:
		result += int(item)
	return result

# print 'my result is', getMiSum(21000)
# print 'math.pow result is', getMathSum(21000)# math.pow()max input number is 1023....
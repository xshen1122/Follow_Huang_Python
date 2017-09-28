# test_xiaobai_4.py
# coding: utf-8
'''
palindromic

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Number = abc * def 
Number = abcdef = fedcba - even digits?? 90009 
这里能写中文了。。。
palindromic是指回文数。比如90009，反过来还是90009
5 digits or 6 digits, number in [10000, 998001]

sublime2没法写中文，我用了github上的fix后，通过subl . 打开sublime可以写中文，但是不能用CTRL+B，不好。
这道题的关键在于：
1. 通过range（1000,100,-1）来反向推导，速度会更快，因为找最大的数。这个最大数为906609 = 913 * 993
'''
def checkPali(number):
	str1 = str(number)
	reverse_str1 = ''
	for i in range(len(str1)-1,-1,-1):
		reverse_str1 += str1[i]
	
	if str1 == reverse_str1:
		return True
	else:
		return False
def checkThreexThree(number):
	for i in range(100,1000):
		if number%i == 0 and number/i in range(100,1000):
			print number , '=', i, '*', number/i
			
			return number
	return 0
def findMaxPali():
	for item in range(998001,10000,-1):
		if checkPali(item):
			if checkThreexThree(item) != 0:

				return item
			

if __name__ == '__main__':
	print findMaxPali()
	
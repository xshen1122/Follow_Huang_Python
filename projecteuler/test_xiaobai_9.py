# test_xiaobai_9.py
# coding: utf-8
'''


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

condition
1. a*a + b*b = c*c
2. a+b+c=1000
该题的思路：
a×a + bxb = cxc
判断条件1：sqrt(axa+bxb)为xx.0的模式。
判断条件2：a+b+sqrt(axa+bxb)==1000
'''
import math
def checkZhengshu(number):
	if str(number)[-1] == '0':
		
		return True
	else:
		return False
def findPythagorean():
	for a in range(1,1000):
		for b in range(1,1000-a):
			result =a*a+b*b
			if checkZhengshu(math.sqrt(result)) and a+b+int(math.sqrt(result))==1000:
				return a, '*', a , '+', b, '*', b, '=', int(math.sqrt(result)),'*', int(math.sqrt(result))
				

print findPythagorean()
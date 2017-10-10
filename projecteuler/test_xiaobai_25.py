# test_xiaobai_25.py
# coding: utf-8
'''
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
from test_xiaobai_16 import *
import math
def Fib(number):
	if number == 1 or number == 2:
		return 1
	else:
		return Fib(number-1)+Fib(number-2)

number = 300
# while True:
# 	if len(str(Fib(number)))> 1000:
# 		print Fib(number)
# 		break
# 	number -= 1


def fib(max):  
	a, b = 1, 1  
	while a < max:  
	    yield a  
	    a, b = b, a+b  
      
def getDigits(number):
	return len(str(number))
      
m = fib(myPow(3500))
while True:

	print getDigits(m.next())
	print m.next() , '->'
'''
制造出非常大的数字，math.pow()都overflow了。
需要用myPow(3500)

'''
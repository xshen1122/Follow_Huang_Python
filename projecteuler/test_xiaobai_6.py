# test_xiaobai_6.py
# coding: utf-8
'''


The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
这道题比较简单。


1*1 + 2*2 +.... + 100*100 = result1
(1+2+3....+100)*(1+2+3+....+100) = result2
diff = result2-result1
'''

def square(number):
	return number*number
result1 = 0
v1 = 0
result2 = 0
for i in range(1,101):
	v1 += i 
result1 = square(v1)

for i in range(1,101):
	result2 += square(i)

print 'the difference between result2 and result1 is ', result1-result2


'''
Output:
the difference between result2 and result1 is  25164150


'''
# test_lintcode_easy_14.py
# coding: utf-8
'''



Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
注意事项

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.

样例

Given num1 = "123", num2 = "45"
return "168"
不能直接将string转为int

'''
def convertString(s1):
	n = len(s1)
	result = 0
	for item in s1:
		result += int(item)*10**(n-1)
		n -= 1
	return result
def addString(s1,s2):
	return convertString(s1) + convertString(s2)
	

if __name__ == '__main__':

	# print convertString('123')
	if addString('123','45')==168:
		print 'Pass'
	else:
		print 'Fail'
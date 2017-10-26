# test_lintcode_10.py
# coding: utf-8
'''


判断一个正整数是不是回文数。

回文数的定义是，将这个数反转之后，得到的数仍然是同一个数。
注意事项

给的数一定保证是32位正整数，但是反转之后的数就未必了。
样例

11, 121, 1, 12321 这些是回文数。

23, 32, 1232 这些不是回文数。
string的切片，反转string， str[::-1]

'''

def findHuiwen(number):
	mystr = str(number)
	
	if mystr == mystr[::-1]:
		return True
	else:
		return False

if __name__ == '__main__':
	if findHuiwen(12321):
		print 'Pass'
	else:
		print 'Fail'
	if findHuiwen(1232):
		print 'Fail'
	else:
		print 'Pass'
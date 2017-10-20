# test_lintcode_easy_02.py
# coding: utf-8
'''



给一个整数 c, 你需要判断是否存在两个整数 a 和 b 使得 a^2 + b^2 = c.
样例

给出 n = 5
返回 true // 1 * 1 + 2 * 2 = 5
给出 n = -5
返回 false


'''

def checkTriage(n):
	for i in range(n):
		for j in range(n):
			if i**2 + j**2 == n:
				return True
	return False

if __name__ == '__main__':
	n = 5
	if checkTriage(n) == True:
		print 'PASS'
	else:
		print 'Fail'
	if checkTriage(9) == False:
		print 'PASS'
	else:
		print 'Fail'
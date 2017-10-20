# test_lintcode_easy_05.py
# coding: utf-8
'''


合并两个排序的整数数组A和B变成一个新的数组。
样例

给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]


'''

def addTwoList(l1,l2):
	
	return sorted(l1+l2)

if __name__ == '__main__':
	A = [1,2,3,4]
	B = [2,4,5,6]
	if addTwoList(A,B) == [1,2,2,3,4,4,5,6]:
		print 'PASS'
	else:
		print 'Fail'



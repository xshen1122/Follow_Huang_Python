# tiaozhan_01.py
# coding: utf-8
'''
给你一个整数列表L,判断L中是否存在相同的数字，
若存在，输出YES，否则输出NO。

'''
def checkList(list1):
	if len(list1) == len(set(list1)):
		return 'No'
	else:
		return 'YES'

if __name__ == '__main__':
	print checkList([1,2,3,4,5,5,6])
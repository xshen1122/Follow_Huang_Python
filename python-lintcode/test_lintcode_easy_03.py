# test_lintcode_easy_03.py
# coding: utf-8
'''


给出两个字符串，你需要找到缺少的字符串
样例

给一个字符串 str1 = This is an example, 给出另一个字符串 str2 = is example
返回 ["This", "an"]



'''
def findMissString(str1,str2):
	l1 = str1.split(' ')
	l2 = str2.split(' ')
	result_list = []
	if len(l1) > len(l2):
		for item in l1:
			if item not in l2:
				result_list.append(item)
	else:
		for item in l2:
			if item not in l1:
				result_list.append(item)
	return result_list
if __name__ == '__main__':
	str1 = 'This is an example'
	str2 = 'is example'
	if findMissString(str1, str2 ) == ['This','an']:
		print 'Pass'
	else:
		print 'Fail'
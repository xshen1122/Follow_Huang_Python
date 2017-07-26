# test_2.py
# coding: utf-8
'''
spread_list([1, 3,[5, 6, [9, 10], [11,[12, [13, 14]]], 15]])
	[1, 3, 5, 6, 9, 10, 11, 12, 13, 14, 15]

思路：
1. 先将数组转换为字符串
2. 通过字符串的替换方法，将[, ]去掉
3. 通过字符串的split方法，用','来分割字符串为list
最后经字符串转换为int，并存到数组里
'''

def spread_list(yourlist):
	return str(yourlist)

result_list = []
list1 = [1, 3,[5, 6, [9, 10], [11,[12, [13, 14]]], 15]]
for item in spread_list(spread_list(list1).replace('[','')).replace(']','').split(','):
	result_list.append(int(item))
print result_list

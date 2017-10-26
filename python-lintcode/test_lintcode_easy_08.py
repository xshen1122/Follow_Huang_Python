# test_lintcode_easy_08.py
# coding: utf-8
'''
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 
target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

如果 source = "source" 和 target = "target"，返回 -1。

如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。
'''
def getSubStr(orignal,sub):
	for i in range(len(orignal)-len(sub)):
		if orignal[i] == sub[0] and original[i:i+len(sub)] == sub:
			return i
	return -1

if __name__ == '__main__':
	orignal = 'source'
	sub = 'target'
	if getSubStr(orignal,sub) == -1:
		print 'Pass'
	else:
		print 'Fail'
	original = 'abcdabcdefg'
	sub = 'bcd'
	if getSubStr(orignal,sub) == -1:
		print 'Pass'
	else:
		print 'Fail'
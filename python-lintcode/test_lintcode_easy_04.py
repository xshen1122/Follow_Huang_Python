# test_lintcode_easy_04.py
# coding:utf-8
'''


给一个字符串,你可以选择在一个字符或两个相邻字符之后拆分字符串,使字符串由仅一个字符或两个字符组成,输出所有可能的结果
样例

给一个字符串"123"
返回[["1","2","3"],["12","3"],["1","23"]]



'''
def seperateStr(str1):
	pass

if __name__ == '__main__':
	str1 = '123'
	if seperateStr(str1) == [['1','2','3'],['12','3'],['1','23']]:
		print 'Pass'
	else:
		print 'Fail'
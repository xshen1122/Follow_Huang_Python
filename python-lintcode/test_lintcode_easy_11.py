# test_lintcode_11.py
# coding: utf-8
'''


给出一个包含大小写字母的字符串。求出由这些字母构成的最长的回文串的长度是多少。

数据是大小写敏感的，也就是说，"Aa" 并不会被认为是一个回文串。
注意事项

假设字符串的长度不会超过 1010。
样例

给出 s = "abccccdd" 返回 7

一种可以构建出来的最长回文串方案是 "dccaccd"。

最大回文字符串，其实就是看不同字符的个数，
只有一个字符是奇数个
其他字符必须是偶数个

'''
def findMaxHuiwen(yourstring):
	word_dict = {}
	max_value = 0
	result = 0
	for item in yourstring:
		if item in word_dict.keys():
			word_dict[item] = word_dict.setdefault(item,1)+1 
			
		else:
			word_dict.setdefault(item,1)
	# print word_dict
	for key in word_dict.keys():
		if word_dict[key] % 2 == 0:
			result += word_dict.get(key)
		else:
			
			if word_dict.get(key) > max_value:
				max_value = word_dict.get(key)
	return result+max_value

if __name__ == '__main__':
	s = "abeecccccdd"
	
	if findMaxHuiwen(s) == 9:
		print 'Pass'
	else:
		print 'Fail'
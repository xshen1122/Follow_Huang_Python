# tips_05.py
# coding: utf-8
'''
请输入一个字符串:
www.runoob.com
请输入一个子字符串:
runoob
1

'''
def findSubString(original,sub):
	first_word=sub[0]
	result = 0
	for i in range(len(original)):
		if original[i] == first_word:
			if original[i:i+len(sub)] == sub:
				result += 1
	return result


if __name__ == '__main__':
	original = 'www.runoob.com.runoob.com.runoob.com.www.com'
	sub = 'com'
	print findSubString(original,sub)
	print original.count(sub) #有时候一句话就能做出来了
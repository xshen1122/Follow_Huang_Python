# test_lintcode_easy_06.py
# coding: utf-8
'''


给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
样例

对于字符串 "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
这道题考验了字符串的切片


'''
def rotateString(offset,str1):
	if offset==0:
		return str1
	else:
		return str1[-offset:] + str1[:len(str1)-offset]

if __name__ == '__main__':
	str1 = 'abcdefg'
	
	
	if rotateString(0,str1) == 'abcdefg' and rotateString(1,str1)=='gabcdef' and rotateString(2,str1)=='fgabcde' and rotateString(3,str1)=='efgabcd':
		print 'PASS'
	else:
		print 'Fail'
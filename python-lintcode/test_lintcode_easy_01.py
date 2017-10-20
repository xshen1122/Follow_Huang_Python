# test_lintcode_easy_01.py
# coding: utf-8
'''
给出两个字符串, 你需要修改第一个字符串，将所有与第二个字符串中相同的字符删除, 
并且第二个字符串中不同的字符与第一个字符串的不同字符连接

给出 s1 = aacdb, s2 = gafd
返回 cbgf
给出 s1 = abcs, s2 = cxzca;
返回 bsxz
'''

def connectStr(str1, str2):
	same_list = []
	new_str1 = ''
	for item in str1:
		if item in str2:
			same_list.append(item)
	
	for item in str1+str2:
		if item not in same_list:
			new_str1 += item

	return new_str1


if __name__ == '__main__':
	s1 = 'aacdb'
	s2 = 'gafd'
	if connectStr(s1,s2) == 'cbgf':
		print 'PASS'
	else:
		print 'Fail'
	s3 = 'abcs'
	s4 = 'cxzca'
	if connectStr(s3,s4) == 'bsxz':
		print 'PASS'
	else:
		print 'Fail'
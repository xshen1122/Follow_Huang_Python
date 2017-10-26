# test_lintcode_easy_17.py
# coding: utf-8
'''


给出一个非负整数 num，反复的将所有位上的数字相加，直到得到一个一位的整数。
样例

给出 num = 38。

相加的过程如下：3 + 8 = 11，1 + 1 = 2。因为 2 只剩下一个数字，所以返回 2。



'''
def convertToList(number):
	number_list = []
	for item in str(number):
		number_list.append(int(item))
	return number_list

def addEachDigit(number):
	
	
	for i in range(3):
		result=0
		for item in convertToList(number):
			result += item
			
		if result < 10:
			return result
		else:
			
			number=result

if __name__ == '__main__':
	
	if addEachDigit(3800000)  == 2:
		print 'Pass'
	else:
		print 'Fail'
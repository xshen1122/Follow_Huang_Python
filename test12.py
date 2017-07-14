# test12.py
# coding: utf-8
'''
有二个递增的list

list1 = [3, 7, 8, 9, 12]

list2 = [5, 6, 10, 13, 25, 30]

合并成一个新的递增list

list3 = [3, 5, 6, 7, 8, 9, 10, 12, 13, 25, 30]

'''
def sort_list2(list1,list2):
	new_list = []
	for item in list1:
		new_list.append(item)
	for item in list2:
		new_list.append(item)
	new_list.sort()
	return new_list
# list1 = [3, 7, 8, 9, 12]
# list2 = [5, 6, 10, 13, 25, 30]
# print sort_list2(list1,list2)

'''
Python 判读是不是等差数列，要求算法时间复杂度为O(NlogN)

'''
def check_if_dengcha(list1):
	if len(list1) < 2:
		return False
	else:
		delta = list1[1]-list1[0]
		previous = list1[0]
		for i in range(1,len(list1)):
			if not list1[i] - previous == delta * i:
				return False
		return True

list1 = []
for i in range(1,10000):
	list1.append(i*2)
list1.append(3300)
print check_if_dengcha(list1)

'''
描述： 输入一个整数N，然后输入N个整数。判断这N个整数是否可以构建一个等差数列。（0<n<1000）
'''
'''
“一个日志文本文件有2000行，提取其中的100行到200行，怎么做？”
'''
def output_100_200():
	myfile = open(r'C:\Users\real-qa\Desktop\TEMP\Logcat_20170707154003.log','r')
	i=0
	for line in myfile.readlines():
		if i>99 and i<201:
			print i,'------>',line
		i = i+ 1
'''
写一个函数，判断字符串是不是由唯一字符组成（由不同的字符组成）
'''
def check_unique_word(str1):
	if str1 == None:
		return 'your str1 should not be None'
	elif str1 == '':
		return 'your str1 should not be empty'
	else:

		for i in range(len(str1)):
			for j in range(i, len(str1)):
				if not str1[j] == str1[i]:
					return False
		return True
def get_dengcha_count(list1):
	'''
	1. 从index=0开始找等差，倒叙找，如果找到了，就将等差数列去掉，再重新找
	2. 如果没有找到，那就从index=1,index=2, index=3, 开始找。
	3. 居然解出来。解决问题。

	'''
	orig_list = list1
	count = 0
	pos=0
	result = True
	index = 0
	if check_if_dengcha(orig_list):
		return 1
	while index < len(orig_list)-1:
		print 'orig list is ',orig_list
		for i in range(len(orig_list)-1,0,-1):
			 if check_if_dengcha(orig_list[:i]):
			 	pos = i
			 	orig_list = orig_list[pos:]
			 	count = count + 1
			 	break
			 else:
			 	orig_list = list1[index+1:]
		index = index + 1

			
			

	return count
	'''
	考虑的太简单，如果是连续的大于3个等差数列，计数错误。
	比如
	list1 = [1,2,4,8,9,10,11,12,13,14]
	这里只有1个长度大于3的等差数列，8,9,10,11,12,13,14。。。

	'''
	# count, total = 1,0
	# if len(list1) < 3:
	# 	return 0
	# i = 1
	# while i < len(list1) -1:
	# 	if list1[i] - list1[i-1] == list1[i+1] - list1[i]:
	# 		total += count
	# 		count +=1
	# 	else:
	# 		count =1
	# 	i += 1
	# return total




def test_check_unique_word():
	str1 = 'aaaaaaaaaaaaaaaaaaa'
	print str1, '--->',check_unique_word(str1)
	str1 = None
	print str1, '--->',check_unique_word(str1)
	str1 = ''
	print str1, '--->',check_unique_word(str1)
	str1 = 'foo'
	print str1, '--->',check_unique_word(str1)
	str1 = 'bar'
	print str1, '--->',check_unique_word(str1)
def test_get_dengcha_count():
	list1 = [1,2,3,9,10,11]
	print get_dengcha_count(list1)

if __name__ == '__main__':
	# test_check_unique_word()
	test_get_dengcha_count()
	
	


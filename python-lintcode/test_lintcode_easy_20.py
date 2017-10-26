# test_lintcode_easy_20.py
# coding: utf-8
'''
移动0，将一个数组中的0全部移到最后面

list1 = [1,0,3,5,8,0,1,6]
list2 = [1,3,5,8,1,6,0,0]

'''
def moveZero(l):
	l1 = []
	zero_time=0
	for item in l:
		if item != 0:
			l1.append(item)
		if item == 0:
			zero_time +=1 
	for i in range(zero_time):
		l1.append(0)
	return l1

if __name__ == '__main__':
	print moveZero([1,0,3,0,5,0,8,0,1,0,6])

# test_xiaobai_1.py
# coding: utf-8
'''
充分信任 Python,大胆设想,小心求证,搜寻己有实例,谁都可以创造出美妙实用的工具!
'''
'''
Question1:


If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


'''
def findThreeFive(number):
	number_list = []
	for item in range(1,number):
		if item%3 == 0 or item%5 == 0:
			number_list.append(item)
	return number_list

if __name__ == '__main__':
	print findThreeFive(1000)
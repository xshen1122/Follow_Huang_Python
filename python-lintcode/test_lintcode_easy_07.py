# test_lintcode_easy_07.py
# coding: utf-8
'''



给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：

    如果这个数被3整除，打印fizz.
    如果这个数被5整除，打印buzz.
    如果这个数能同时被3和5整除，打印fizz buzz.

样例

比如 n = 15, 返回一个字符串数组：

[
  "1", "2", "fizz",
  "4", "buzz", "fizz",
  "7", "8", "fizz",
  "buzz", "11", "fizz",
  "13", "14", "fizz buzz"
]



'''
def printBuzzFizz(number):
	result_list = []
	for i in range(1,number+1):
		if i%3 == 0 and i%15 !=0:
			result_list.append('fizz')
		elif i%5 == 0 and i%15 !=0:
			result_list.append('buzz')
		elif i%15 == 0:
			result_list.append('fizz buzz')
		else:
			result_list.append(str(i))
	return result_list


if __name__ == '__main__':
	print printBuzzFizz(15)
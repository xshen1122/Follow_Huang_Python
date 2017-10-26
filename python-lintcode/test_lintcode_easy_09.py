# test_lintcode_easy_09.py
# coding: utf-8
'''
Given dict = ["picture", "turepic", "icturep", "word", "ordw", "lint"]
return 3.

"picture", "turepic", "icturep" are same ratote words.
"word", "ordw" are same too.
"lint" is the third word that different from the previous two words.

'''
from test_lintcode_easy_06 import *
def findRotateString(list1):
	result = 0
	dup_list = list1
	for item in list1:
		for offset in range(len(item)):
			print rotateString(offset,item)
			if rotateString(offset,item) in list1:
				result += 1
				list1.remove(rotateString(offset,item))
				break

				
			
	return result

if __name__ == '__main__':
	list1 = ["picture", "turepic", "icturep", "word", "ordw", "lint","tlin","ntli"]
	print findRotateString(list1)

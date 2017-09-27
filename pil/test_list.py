# test_list.py
# coding: utf-8
'''
假设我有这样两个list，

          一个是list1，list1 = [1, 2, 3, 4, 5]
          一个是list2，list2 = [1, 4, 5]
          我们如何得到一个新的list，list3，
          list3中包括所有不在list2中出现的list1中的元素。
          即：list3 = list1 – list2

using set <==> list
'''
list1 = [1, 2, 3, 4, 5]
list2 = [1, 4, 5]

def add(list1, list2):
	list3 = []
	for item in list1:
		list3.append(item)
	for item in list2:
		list3.append(item)
	return list(set(list3))

print add(list1, list2)
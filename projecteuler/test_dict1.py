# test_dict.py
# coding: utf-8
word = ['A','C','B','B']
number = ['1','1','0','0']
dict1 =  dict(zip(word,number))
value_list = []
for key in dict1.keys():
	value_list.append(dict1[key])

if len(value_list) > len(set(value_list)):
	print 'dup'
else:
	print 'ok'
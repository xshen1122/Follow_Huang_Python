# test.py
# coding: utf-8
word_dict={}
yourstring='abcdddac'
for item in yourstring:
		if item in word_dict.keys():
			
			word_dict.get(item) = 2
		else:
			word_dict.setdefault(item,1)
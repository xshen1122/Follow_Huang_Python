# test_occur_number.py
# coding: utf-8

'''
record how much times for each word

Key points:
1. dict.fromkeys(List)  ---> keys = List
2. dict.keys()  --- keys List
3. dict[key] -- value
4. print top3
'''
str1 = 'hello, friends, welcome to Beijing, this is a wonderful world'
str_list = []
str_dict = {}
for word in str1.lower():
	str_list.append(word)
str_set = set(str_list)
str_dict = dict.fromkeys(str_set)
for item in str_dict.keys():
	str_dict[item] = str1.count(item)
print str_dict

# using sorted(dic.iteritems(), key, reverse)
new_dict= sorted(str_dict.iteritems(), key=lambda d:d[1], reverse = True)

print new_dict[:10]
# test_xiaobai_22.py
# coding: utf-8
'''


Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

用字典非常好处理，需要记住key和value的情况

'''
def getXishu(yourname):
	NAME_MAP = {}
	result = 0
	NAME_LIST = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	for i in range(1,27):
		NAME_MAP.setdefault(NAME_LIST[i-1],i)
	for item in yourname:
		result += NAME_MAP[item]
	return result

print getXishu('COLIN')

temp_name_list= []
name_list = []
name_dict = {}
myfile= open('p022_names.txt','r')
for line in myfile.readlines():
	temp_name_list = (line.split(','))
for item in temp_name_list:
	name_list.append(item[1:-1])

for i in range(len(name_list)):
	name_dict.setdefault(name_list[i],[i+1,getXishu(name_list[i]),(i+1)*getXishu(name_list[i])])

print name_dict['COLIN'], name_dict['COLIN'][2]


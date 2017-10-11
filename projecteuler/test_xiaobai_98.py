# test_xiaobai_98.py
# coding:utf-8
'''
将单词CARE中的四个字母依次赋值为1、2、9、6，我们得到了一个平方数：1296 = 362。神奇的是，使用同样的数字赋值，重排后的单词RACE同样构成了一个平方数：9216 = 962。我们称CARE和RACE为重排平方单词对，同时规定这样的单词对不允许有前导零或是不同的字母赋相同的值。

在这个16K的文本文件words.txt（右击并选择“目标另存为……”）中包含了将近两千个常见英文单词，找出所有的重排平方单词对（一个回文单词不视为它自己的重排）。

重排平方单词对所给出的最大平方数是多少？

注意：所有的重排单词必须出现在给定的文本文件中。

1.words文件中找出又相同字母组成的单词对

2.构造平方数，筛选由相同数字组成的平方数

3.关键的就是单词和数字的映射关系，特别是位置要做到对应，但是我只能保证字母和数字映射后，可以组成的数字是平方数，但是数字的顺序字母映射的顺序不一样，造成输出的结果比较多。


找映射关系比较复杂了，比如ACT，CAT
A 可以在【1-9】，C可以在【1-9】，T可以在【0-9】
三次循环遍历出各种组合，然后每个去匹配是否为平方数。。。

Idea：
或者可以反过来，看看三位数的平方数有哪些，然后找出来符合ACT，CAT规律的，就是前两位互相调换位置。

或者可以反过来，看看三位数的平方数有哪些，然后找出来符合ACT，CAT规律的。找mapping关系可以通过字典来找。
'''
import math
def checkSquare(number):
	if str(math.sqrt(number))[-1] == '0':
		return True
	else:
		return False
def compareSquareWords(str1, str2):
	l1 = []
	l2 = []
	for item in str1:
		l1.append(item)
	for item in str2:
		l2.append(item)
	if len(l1) == len(l2) and sorted(l1) == sorted(l2):
		return True
	else:
		return False

def processWordList(yourfile='p098_words.txt'):
		tmp_list = []
		word_list = []
		result_list = []
		myfile = open(yourfile,'r')
		for line in myfile.readlines():
			tmp_list = line.split(',')

		for item in tmp_list:
			word_list.append(item[1:-1])

		for i in range(len(word_list)):
			for j in range(i,len(word_list)):
				if compareSquareWords(word_list[i],word_list[j]) and word_list[i] != word_list[j]:
					result_list.append([word_list[i],word_list[j]])
		myfile.close()
		return result_list

def find3DigitsSquare(number):
	tmp_list = []
	for i in range(number,number*10):
		if checkSquare(i):
			tmp_list.append(str(i))
	return tmp_list

def getFirstList(item_in_result_list):
	first_list = []
	
	for item in item_in_result_list[0]:
		first_list.append(item)
	return first_list
	
def getSecondList(item_in_result_list):
	second_list = []
	for item in item_in_result_list[1]:
		second_list.append(item)
	return second_list
def getNumberList(number):
	number_list = []
	for item in str(number):
		number_list.append(item)
	return number_list
def checkDictOK(dict1):
	value_list = []
	for item in dict1.keys():
		value_list.append(dict1[item])
	if len(value_list) > len(set(value_list)):
		return False
	else:
		return True

def process(test_list,pair_list):

	for item_n in find3DigitsSquare(10**(len(test_list)-1)):
		new_str = ''
		item_list = getNumberList(item_n)
		item_dict = dict(zip(test_list,item_list))
		# print item_dict
		pool_list =  find3DigitsSquare(10**(len(test_list)-1))
		
		for item in pair_list:
			new_str += item_dict[item]
		# print item_n, new_str,pool_list
		if (new_str) in pool_list and checkDictOK(item_dict):
			print 'Got it', item_n, new_str,test_list,pair_list
		else:
			pass
if __name__ == '__main__':
	# test_list = ['C','A','R','E']
	# pair_list = ['R','A','C','E']

	for item in processWordList():
		test_list = getFirstList(item)
		pair_list = getSecondList(item)
		process(test_list,pair_list)

'''
OUTPUT:
Got it 17689 18769 ['B', 'O', 'A', 'R', 'D'] ['B', 'R', 'O', 'A', 'D']
Got it 1296 9216 ['C', 'A', 'R', 'E'] ['R', 'A', 'C', 'E']
Got it 9216 1296 ['C', 'A', 'R', 'E'] ['R', 'A', 'C', 'E']


'''

	
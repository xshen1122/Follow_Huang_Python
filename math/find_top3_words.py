# find_top3_words.py
# coding: utf-8
'''
English Noval:gone with wind
Top 3 Words
1. read file
2. split Words
3. sorted 
4. show up
'''
def showTop3Word(yourfile):
	pass

def removeSymbol(str1):
	new_item=''
	for item in str1:
		if item.isalpha():
			new_item += item

	return new_item
def addWord(theIndex,word,pagenumber): 
  theIndex.setdefault(word, [ ]).append(pagenumber)

if __name__ == '__main__':
	myfile = open('gone1.txt','r')
	word_list = []
	for line in myfile.readlines():

		for item in line.split():
			if item.isalpha:
				word_list.append(removeSymbol(item))
	new_word_list = []
	for item in word_list:
		if item=='':
			pass
		else:
			new_word_list.append(item)


	word_dir={}
	for item in new_word_list:
		if item in word_dir.keys():
			
			word_dir[item] = word_dir.setdefault(item) + 1
			
		else:
			word_dir.setdefault(item,1)

	print sorted(word_dir.items(),key=lambda d: d[1],reverse=True) # This is sorting

	# dict setdefault() is very good.
	'''
	使用 setdefault 方法相当于如下的操作：

	if key in dict:
	 reurn dict[key]
	else:
	 dict[key] = default
	 return default




	'''
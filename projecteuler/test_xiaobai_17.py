# test_xiaobai_17.py
# coding: utf-8
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 

'''


def getLetter(yourlist):
	ss=''
	for item in yourlist:
		ss += item
	return len(ss)
def getList(yourlist):
	for item in one_digit[:-1]:
		yourlist.append(yourlist[0]+item)
	return yourlist


if __name__ == '__main__':
	one_digit = ['one','two','three','four','five','six','seven','eight','nine','ten']
	teenage_digit = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	twenty_digit = ['twenty']
	thirty_digit = ['thirty']
	forty_digit = ['forty']
	fifty_digit = ['fifty']
	sixty_digit = ['sixty']
	seventy_digit = ['seventy']
	eighty_digit = ['eighty']
	ninety_digit = ['ninety']
	hundred_digit = ['hundredand']
	letter_list = []
	letter_list.append(getLetter(one_digit))
	letter_list.append(getLetter(getList(twenty_digit)))
	letter_list.append(getLetter(getList(thirty_digit)))
	letter_list.append(getLetter(getList(forty_digit)))
	letter_list.append(getLetter(getList(fifty_digit)))
	letter_list.append(getLetter(getList(sixty_digit)))
	letter_list.append(getLetter(getList(seventy_digit)))
	letter_list.append(getLetter(getList(eighty_digit)))
	letter_list.append(getLetter(getList(ninety_digit)))
	result = 0
	for item in letter_list:
		result += item
	print result # 1-99 has 787 letters
	# 100 - 199 has ??
	#以下就按100-199，200-299， 900-999,1000来计数即可

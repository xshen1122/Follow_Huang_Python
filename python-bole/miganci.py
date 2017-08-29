# miganci.py
# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


your_input='你娘的jiangge，无数看风景的人'

def check_miganci(yourstring):
	miganci_list = [
			'北京',
			'程序员',
			'公务员',
			'领导',
			'牛比',
			'牛逼',
			'你娘',
			'你妈',
			'love',
			'sex',
			'jiangge'
			]
	newstring = yourstring
	for item in miganci_list:
		if item in yourstring:
			return 'Freedom'
			# newstring = newstring.replace(item,'**')
			# print newstring
	return 'Human Rights'
	
	

print check_miganci(your_input)
# string_tricks.py
# coding: utf-8
'''
String
这就是利用 Python 遇到未闭合的小括号时会自动将多行代码拼接为一行和把相邻的两
个字符串字面量拼接在一起的特性做到的

is :  isalnum, isdigit, isalpha, islower, isupper, isspace, istitle, 
with: startwith, endwith

'''
str1 = ('if you are still breathing'
	    'it is not too late'
	    'get up and get going'
	    )

s2 ='Get up'
print s2.istitle()
print str1
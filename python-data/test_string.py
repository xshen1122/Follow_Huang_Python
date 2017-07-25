# test_string.py
# coding: utf-8

from test_stack_1 import Stack

print dir('aaa')
'''
常用的方法：
upper, lower - 转换大小写
isdigit, islower, isupper, isspace, isalpha - 判断字符类型
endswith, startswith - 判断以xx开头，以xx结尾
join - 将字符串和list连起来
split - 以空格或者逗号来分解字符串
count - 统计字符串出现的次数
index - 字符串出现的位置
replace - 字符串替换
find - 字符串查找
没有reverse啊
'''

mystr = 'gone with the wind'
s1 = 'goodgoogle'
print mystr.count('th')
print mystr.index('th')
print s1.find('goo')

def reverse(mystr):
	s1 = Stack()
	for item in mystr:
		s1.push(item)
	while len(s1) != 0:
		print s1[-1]
		s1.pop()
reverse(mystr)
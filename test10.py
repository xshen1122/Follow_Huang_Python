# test10.py
# coding:utf-8
'''
使用os.system()来执行命令

'''
import os
# if os.name == 'nt':
# 	command = 'dir'
# else:
# 	command = 'ls'

# os.system(command)
import string
# str1 = 'Gone in the wind'
# print 'Upper ---->', string.upper(str1) #两种写法，str1.upper(), string.upper(str1)
# print 'Lower ---->', str1.lower()
# print 'Split ---->', str1.split()
# print 'Join ----->', string.join(string.split(str1),'+')#两个参数，把list的每一个item和B连起来
# print 'Replace --->', str1.replace('Gone','Welcome') #返回一个新的string，不会改变老string
# print 'Replace2 -->',string.replace(str1,'Gone','Goodbye')
# print 'Find ---->',str1.find('wind')
# print 'Count ---->',string.count(str1,'in') #在字符串中有几个'in'

# print '================================'
# print 'Join2 ------>',"+".join(str1.split())
# print 'Count2 ----->',str1.count('n')


import math
# print 'PI is ', math.pi
# print 'e is ', math.e
# print 'hypot is ', math.hypot(12.0,13.0)

import copy
# mylist = [1,2,3,4,5]
# l1 = copy.copy(mylist)
# print l1
# l2 = copy.deepcopy(mylist)
# print l2


import sys
# print len(sys.path)

# # print sys.modules.keys()
# var = '1234'
# print sys.getrefcount(0)
# print sys.getrefcount(var)
# print sys.getrefcount(None)

'''
学习stdin，stdout

'''
import string
# class Redirect:
# 	def __init__(self, stdout):
# 		self.stdout = stdout # 把stdout传入
# 	def write(self,s):
# 		self.stdout.write(string.lower(s)) # 输出小写字母


# old_stdout = sys.stdout
# sys.stdout = Redirect(sys.stdout)

# print 'HELLO GOODBYE GREAT WALL'
# print 'FIRST SECOND \303\226R'

# # restore to back
# sys.stdout= old_stdout
# print 'HELLO GOODBYE GREAT WALL'
# print 'FIRST SECOND \303\226R'

'''

学习time的用法，特别是strftime

'''
import time
now = time.localtime()
print time.strftime("%y%m%d  %H:%M:%S", now)
print time.strftime("%a %b %d", now)
print time.strftime("%c", now)
print time.strftime("%I %p", now)
print time.strftime("%Y-%m-%d %H:%M:%S %Z", now)

'''
time的另一种方法：timing

'''

def procedure():
	time.sleep(2.5)
t1 = time.clock()
procedure()
print time.clock()-t1

t1 = time.time()
procedure()
print time.time()-t1
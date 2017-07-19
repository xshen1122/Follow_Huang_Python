# test14.py
# coding: utf-8
'''

print中，python支持用，（逗号）将不同类型的变量隔开，一起打印出出来
'''

Date = '2017-07-17'
value = 4
benefit = 6.8
print 'Today is ', Date, value, benefit
print 'Today is %s, value is %d, benefit is %f' % (Date, value, benefit) #后面必须是元组

print '.' * 10  #连续打印出10个，这在打印菱形的题目中很有用

formatter = '%r--%r--%r--%r' #打印出所有字符
formatter1 = '%s--%s--%s--%s'
print formatter % (1, 2, 3, 4)
str1 = 'one'
print formatter1 % (str1,'two','three','four')

#转移符
print 'for \' we need \\,for \", we need \\, for /, we dont need \\'

# 从键盘读取输入
print 'Please input your gender, Female or Male?', #在这里加了一个逗号，光标不会跑到下一行
gender = raw_input()
print gender

# 或者可以在raw_input()里面给出提示
name = raw_input('Please input your Name')
print name
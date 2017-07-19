# test15.py
# coding: utf-8
'''
参数的用法，argv-参数变量
解包：将argv解出来一次赋给左边的script，one，two，three
运行为：python test15.py a b c 
script名为test15.py, 参数1,2,3分别为a，b，c
argv是一个list，包含了script和参数1,2,3... 
'''
from sys import argv
script, one,two,three = argv
print script
print one
print two
print three
print argv

# 带参数的脚本，用ctrl+B就不行了。ctrl+B相当于python test13.py的快捷键
lines = '''

今天是个好日子
高兴的事儿真真多
今天是个好日子
啦啦啦啦啦啦啦   

'''
# 三个引号，无论单双，都是可以包含多行字符串
print lines

'''
文件的read-把所有内容读进来
文件的readlines - 将文件内容按行读入
文件的readline - 读取一行

'''

'''
函数的*args, **kwargs从哪里来的？
参考argv来的
比如def func(*args):
    sys1,sys2 = args
允许输入2个参数

'''
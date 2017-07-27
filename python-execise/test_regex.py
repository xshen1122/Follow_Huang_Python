# test_regex.py
# coding: utf-8
'''
<.*>会把所有字符吞下满足前面是<后面是>就返回字符串
<.*?>一次吃一个字符满足条件返回字符串 
a.*?b匹配最短的，以a开始，以b结束的字符串。如果把它应用于aabab的话，
它会匹配aab（第一到第三个字符）和ab（第四到第五个字符）。
'''
import re
str1 = 'aabab'
pattern = 'a.*?b'
print re.findall(pattern,str1)
print re.search(pattern,str1).group()

pattern2 = 'a.*b'
print re.findall(pattern2,str1)
print re.search(pattern2,str1).group()
# tiaozhan_02.py
# coding: utf-8
'''

OrderedDict，实现了对字典对象中元素的排序

'''
import collections
print "Regular dictionary"
d={}
d['a']='1'
d['b']='2'
d['c']='3'
for k,v in d.items():
    print k,v

print "\nOrder dictionary"
d1 = collections.OrderedDict()
d1['a'] = 1
d1['b'] = 2
d1['c'] = 3
d1['e'] = 4
d1['f'] = 5
for k,v in d1.items():
    print k,v
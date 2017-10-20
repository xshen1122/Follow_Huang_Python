# tips_07.py
# coding:utf-8
'''
time.clock(): 获取毫秒信息

'''
import time
start = time.clock()

for i in range(10000):
    print i
end = time.clock()
print start, end
print 'different is %6.3f' % (end - start)
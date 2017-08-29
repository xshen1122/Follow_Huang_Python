# algorithm_complexity.py
# coding: utf-8
'''
算法复杂度
'''
def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]
import cProfile
import random

if __name__ == '__main__':
	
	lIn = [random.random() for i in range(100000)]
	cProfile.run('f1(lIn)')
	cProfile.run('f2(lIn)')
	cProfile.run('f3(lIn)')

#从运行时间来看，f1需要0.053秒，f2需要0.031秒，f3需要0.057秒。那么f2最好，f1次之，f3最差
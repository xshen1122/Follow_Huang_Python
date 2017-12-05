# test_counter.py
# coding: utf-8
from collections import Counter
l1 = [1,2,3,4,3,3,3,4,5]
print Counter(l1)
'''
OUTPUT:
Counter({3: 4, 4: 2, 1: 1, 2: 1, 5: 1})

'''
print Counter('success')
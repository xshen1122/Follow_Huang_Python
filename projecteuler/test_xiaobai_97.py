# test_xiaobai_97.py
# coding: utf-8
'''


The first known prime found to exceed one million digits was discovered in 1999, 
and is a Mersenne prime of the form 2mi6972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 
2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.

哇，用%10000000000的方法可以快速得到结果。。。

'''

from test_xiaobai_16 import *
# result = 28433 * myPow(7830457) + 1
# print str(result)[-10:-1]

print ((28433*(2**7830457))+1)%10000000000
'''
OUTPUT:
8739992577

'''


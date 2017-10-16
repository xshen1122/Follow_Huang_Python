# test_s_02.py
# coding: utf-8
'''
'argmax, argmin', 最小值和最大值的索引


'''
import numpy as np
scores =      [31, 24, 23, 25, 14, 25, 13, 12, 14, 23,  
               32, 34, 43, 41, 21, 23, 26, 26, 34, 42,  
               43, 25, 24, 23, 24, 44, 23, 14, 52, 32,  
               42, 44, 35, 28, 17, 21, 32, 42, 12, 34] 
print 'range is ', np.max(scores)-np.min(scores)
print 'avg is ', np.mean(scores)
print 'std is ', np.std(scores)
print 'var is ', np.std(scores)**2
print 'var is ', np.var(scores)
print 'argmax, argmin', np.argmax(scores), np.argmin(scores)
print 'cumsum is ', np.cumsum(scores)
print 'cumprod is', np.cumprod(scores)
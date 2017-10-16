# test_s_001.py
# coding: utf-8
'''
均值(mean)：数据组中所有数值的总和除以该组数值的个数。 

中位数(median)：一系列数据的中点。中位数对极值不敏感，均值对极值敏感。

众数(mode) ：出现数据最多的数值。如果每个数字都相同则没有众数。

在numpy中有直接求总和、平均数、中位数、最大值、最小值的函数，但没有找到求众数的函数
numpy 可以理解为math一样的类，在程序中可以直接调用numpy.max()，获取list中最大的数。
更方便的写法是import numpy as np, 这样可以少写点np.max()


dict的setdefault很好用。如果有这个key，则返回value，如果没有，则在字典中添加这个key
'''
import numpy as np  
import operator  
scores =      [31, 24, 23, 25, 14, 25, 13, 12, 14, 23,  
               32, 34, 43, 41, 21, 23, 26, 26, 34, 42,  
               43, 25, 24, 23, 24, 44, 23, 14, 52, 32,  
               42, 44, 35, 28, 17, 21, 32, 42, 12, 34]  
  
def findmode(values):  
    bucket = {}  
    for value in values:  
        if bucket.has_key(value):  
            bucket[value] += 1  
        else:  
            bucket.setdefault(value,1)  
    bucket = sorted(bucket.iteritems(),key=operator.itemgetter(1),reverse=True)  
      
    modes  = []  
    for value in bucket:  
        if len(modes) == 0:  
            modes.append(value)  
        else:  
            temp = modes[len(modes)-1][1]  
            if temp == value[1]:  
                modes.append(value)  
            else:  
                break  
    return modes  
  
print 'max: \t', np.max(scores)  
print 'min: \t', np.min(scores)  
print 'sum: \t', np.sum(scores)  
print 'mean:\t', np.mean(scores)  
print 'median:\t', np.median(scores)  
modes = findmode(scores)  
print 'mode:\t', modes  

#====================MY=====================#
print 'my max is ', np.max(scores)
print 'my min is ', min(scores)
print 'my sum is ', sum(scores)
print 'my avg is ', float(sum(scores)/(len(scores)))
def findMyMode(scores):
	scores_dict={}
	for item in scores:
		if item in scores_dict.keys():
			scores_dict[item] += 1
		else:
			scores_dict.setdefault(item,1)
	
	return sorted(scores_dict.items(),key=lambda d:d[1],reverse=True)[0]

print findMyMode(scores)
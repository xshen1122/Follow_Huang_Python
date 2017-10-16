# test_s_05.py
# coding: utf-8
'''
首先是引入pandas和numpy，这是经常配合使用的两个包，pandas依赖于numpy，
引入以后我们可以直接使用np/pd来表示这个两个模块
How to use DataFrame
round(float_number, weishu)
第一个参数是一个浮点数，第二个参数是保留的小数位数，可选，如果不写的话默认保留到整数。
round()是取了浮点数的近似数。
print round(120.3456,2) ==> 120.35
创建矩阵: np.random.randn(6,4),
而DataFrame是把矩阵包装成excel表的形式，有每一列的名称，也有每一行的日期。 
pd.date_range('20140729',periods=6)
'''
import pandas as pd
import numpy as np
import scipy.stats.stats as stats  
import math  

def test1():
	score=[  
	       [3,5,1,4,1],  
	       [4,4,3,5,3],  
	       [3,4,4,4,4],  
	       [3,3,5,2,1],  
	       [3,4,5,4,3],  
	       [4,5,5,3,2],  
	       [2,5,5,3,4],  
	       [3,4,4,2,4],  
	       [3,5,4,4,3],  
	       [3,3,2,3,2]]  
	df = pd.DataFrame(score)  
	print type(df)
	total_row = df.sum(axis=1)  
#print total_row  
	sy = total_row.var()  
	print sy   
	var_column =  df.var()  
	si = var_column.sum()  
	print si   
	r = (5.0/4.0)*((sy-si)/sy)  
	print round(r,2)  
	print round(120.3456,2)

def test2():
	dates = pd.date_range('20140729',periods=6)
	print dates
	df = pd.DataFrame(np.random.randn(6,4),index=dates, columns=list('ABCD'))
	print df
	print df.head(3)
	print df.tail(2)
'''
OUTPUT:
                   A         B         C         D
2014-07-29  1.233666  1.137473  1.499147  0.036455
2014-07-30  0.290713 -1.664880 -2.211165 -0.183096
2014-07-31  0.682239 -0.306749 -0.782653 -1.325083
2014-08-01 -0.455287 -0.596243 -0.883513  1.195904
2014-08-02 -0.794822 -0.808185 -0.335095  1.383959
2014-08-03  1.483409 -0.131634 -0.837433 -0.673534

'''
if __name__ == '__main__':
	test2()
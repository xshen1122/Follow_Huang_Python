# test_s_04.py
# coding: utf-8
'''
直接用scipy.stats.stats的pearsonr函数，也可以自己实现计算过程。 简单相关系数
一种简单直观的表示相关的方式是建立所谓的散点图(scatterplot

'''

import scipy.stats.stats as stats 
import matplotlib.pylab as plt 
def test1():
    x=[2,4,5,6,4,7,8,5,6,7]  
    y=[3,2,6,5,3,6,5,4,4,5]  
    r=stats.pearsonr(x,y)[0] 
    print r
def test2():     
    x=[2,4,5,6,4,7,8,5,6,7]  
    y=[3,2,6,5,3,6,5,4,4,5]  
    plt.xlim(0,9)  
    plt.ylim(1,7)  
    plt.xlabel('x axis')  
    plt.ylabel('y axis')  
    plt.plot(x,y,'ro')  
    plt.show()  
def test3():
    s1=[54,67,67,83,87,89,84,90,98,65]  
    s2=[56,77,87,89,89,90,87,92,99,76]  
    r=stats.pearsonr(s1,s2)[0]  
    print r 
    '''
    OUTPUT: 0.9 ==>强相关性

    ''' 

def test4():
    a=[4,5,3,6,7,5,6,4,3,3]  
    b=[5,6,5,6,7,6,7,8,7,7]  
    r=stats.pearsonr(a,b)[0]  
    print r  


    '''
    OUTPUT:
    0.128697890418 ==> 弱相关性

    '''
if __name__ == '__main__':
	test4()
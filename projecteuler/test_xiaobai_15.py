# test_xiaobai_15.py
# coding:utf-8
import sys
sys.setrecursionlimit(1000000)
'''
Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

又是一道网格题。2x2的格子，只能往右或者往下，有多少种不同的路径从左上到右下？（6种）
如果是20x20的网格呢？
1. 怎么将题目抽象为数学算法？
笛卡尔坐标系？？可以分为x方向和y方向
x方向只能+1，y方向只能-1
x从0,1,2，y从2,0,1
第一种方法：  向右走一格（有三种方式到达右下角）
            向下走一格（有两种方式到达右下角）
	        向下走两格（有一种方式到达右下角）
这个有规律不？

递归法：f（n,n)=f(n-1,n)+f(n,n-1)
2x2的格子实际有3个点，所以f（3,3）=6
Issue1:
在网上查了，发现python默认的递归深度是很有限的，
大概是900多的样子，当递归深度超过这个值的时候，就会引发这样的一个异常。
Resolve:
if n==1 or m == 1: 不会出现 m 或者 n 为0的情况
'''
def grid_router(n,m):
	if n==1 or m == 1: 
		return 1
	else:
		return grid_router(m,n-1) + grid_router(m-1,n)

if __name__ == '__main__':
	print grid_router(3,3)
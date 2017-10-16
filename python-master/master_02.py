# master_02.py
# coding: utf-8
'''
itertools - 标准库之一
1. 创建无限迭代器 itertools.count(1),以1为间隔的等差数列
2. 创建无限迭代器 itertools.cycle('ABC'), 以ABC为循环的数列
3. 创建有限迭代器 itertools.repeat('A',10), 循环A 10次
4. 可以通过takewhile截取
比如 n= itertools.count(1)
     ns = itertools.takewhile(lambda x: x<10, n)

5. chain()可以将2个迭代器连起来：
   n1 = itertools.cycle('ABC')
   n2 = itertools.cycle('XYZ')
   itertools.chain(n1, n2)
6. 注意：迭代器定义的时候是不产生无限个迭代元素的，只有在for语句中才产生。

7. groupby可以把迭代器中相邻的重复元素挑出来放在一起

8. itertools的使用示例：
可以用简单的一句话做成4个元素的排列组合
races = itertools.permutations(horse)

'''
import itertools
def test1():
	n = itertools.count(1)
	for i in n:
		print i
# will create an inf list

def raceHorse():
	horse =['a','b','c','d']
	races = itertools.permutations(horse)
	print races
	print list(races)
	print type(list(races))
	
	
def raceNumber():
	print list(itertools.permutations([1,2,3,4],2))	


if __name__ == '__main__':
	raceHorse()
	raceNumber()
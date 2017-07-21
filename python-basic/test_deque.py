# test_deque.py
# coding: utf-8
'''
collections的deque是双向队列
双向队列的API
方法 	描述
append(x) 	    在队列的右边添加一个元素
appendleft(x) 	在队列的左边添加一个元素
clear() 	    从队列中删除所有元素
copy() 	        返回一个浅拷贝的副本
count(value) 	返回值在队列中出现的次数
extend([x..]) 	使用可迭代的元素扩展队列的右侧
extendleft([x..]) 	使用可迭代的元素扩展队列的右侧
index(value, [start, [stop]]) 	返回值的第一个索引，如果值不存在，则引发ValueError。
insert(index, object) 	在索引之前插入对象
maxlen 	           获取队列的最大长度
pop() 	           删除并返回最右侧的元素
popleft() 	       删除并返回最左侧的元素
remove(value) 	   删除查找到的第一个值
reverse() 	       队列中的所有元素进行翻转
rotate() 	       向右旋转队列n步（默认n = 1），如果n为负，向左旋转。

'''
from collections import deque 
'''
杨辉三角形： 编写程序，求二项式系数表中(杨辉三角)第K层系列数
思路
    把第K行的系数存储在队列中
    依次出队K层的系数（每行最后一个1不出队），并推算K+1层系数，添加到队尾，最后在队尾添加一个1，便变成了k+1行。
  1
  1  1
 1  2  1
1 3  3  1
难点：1：两次循环
2. q.append(q.popleft()+q[0])

when k = 3
[1]
[1, 2] - 相当取出左边的第一个元素+1，加到队尾
[2, 1, 3]
[1, 3, 3]
[1, 3, 3, 1]
''' 
def test_deque():
	q = deque([1])
	print q
	q.append(2)
	print q
	q.appendleft(0)
	print q
	q.pop()
	print q
	q.popleft()
	print q
	print not q
	q.clear()
	print not q
def yanghui_my(k):
	q = deque([1])
	for i in range(k):
		for j in range(i):
			q.append(q.popleft()+q[0])
			print list(q)
		q.append(1)
	return list(q)
def yanghui(k):
    """
    :param k: 杨辉三角中第几层
    :return: 第K层的系数
    """
    q = deque([1])  # 创建一个队列，默认从1开始
    for i in range(k):  # 迭代要查找的层数
        for _ in range(i):  # 循环需要出队多少次
            q.append(q.popleft() + q[0])  # 第一个数加上队列中第二个数并赋值到队列末尾
        q.append(1)  # 每次查找结束后都需要在队列最右边添加个1
    return list(q)

def loop_times(k):
	counts = 0
	for i in range(k):
		for j in range(i):
			counts = counts + 1
			print counts
	return counts

if __name__ == '__main__':
	# print yanghui_my(3)
	print loop_times(4)

'''
底下两个例子更难，参考
http://python.jobbole.com/87577/?utm_source=blog.jobbole.com&utm_medium=relatedPosts

'''


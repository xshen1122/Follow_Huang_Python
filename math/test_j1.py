# test_j1.py
# coding: utf-8
'''
(1) 写一个程序,打印出 1 到 100 间的整数。 
(2) 修改练习(1),在值为 47 时用一个 break 退出程序。亦可换成 return 试试。 
(3) 创建一个 switch 语句,为每一种 case 都显示一条消息。并将 switch 置入一个 for 循环里,令其尝试每
一种 case。在每个 case 后面都放置一个 break,并对其进行测试。然后,删除 break,看看会有什么情况出
现。

'''

def print_100():
	for i in range(1,101):
		if i==47:
			return
		print i



if __name__ == '__main__':
	print_100()
# test_stack.py
# coding: utf-8
'''
stack - 特点
特殊的有序表
插入，删除都在栈顶操作
先进后出
可以类比为手枪的弹夹

stack在python里是一类特殊的list

'''

# 创建一个stack
s = []

# 入栈
s.append('a')
s.append('b')
s.append('c')

print s
#出栈
s.pop()
s.pop()
# 判断stack是否为空
print not s
# stack的长度
print len(s)

# 找到栈顶元素
print s[-1]

# 下面有四个例题，在现实中如何使用stack
'''
编写一个函数，判断一个表达式字符串，括号匹配是否正确

思路

    创建一个空栈，用来存储尚未找到的左括号；
    便利字符串，遇到左括号则压栈，遇到右括号则出栈一个左括号进行匹配；
    在第二步骤过程中，如果空栈情况下遇到右括号，说明缺少左括号，不匹配；
    在第二步骤遍历结束时，栈不为空，说明缺少右括号，不匹配

我的code有2个错误的地方
1. 在if not left_stack or not 1 <= ord(word) - ord(left_stack[-1]) <= 2:
这里学会：用ord('[')-ord(']')匹配左括号和有括号
2. return not left_stack #写错2个地方
'''

 	
test1 = '{()[()]},[{({})}]'
test2 ='[(]),[()),(()}'

def check_kuohao(test):
	left_stack = []
	for word in test:
		print left_stack
		if word in ['{','[','(']:
			left_stack.append(word)
		elif word in ['}',']',')']:
			if not left_stack or not 1 <= ord(word) - ord(left_stack[-1]) <= 2:
				return False
			
			left_stack.pop()
	# if not left_stack == False:
	# 	return False
	# else:
	# 	return True
	return not left_stack #写错2个地方

# print check_kuohao(test1)
print check_kuohao(test1)

'''
对比别人的解题


'''
LEFT = {'(', '[', '{'}  # 左括号
RIGHT = {')', ']', '}'}  # 右括号
def match(expr):
    """
    :param expr:  传过来的字符串
    :return:  返回是否是正确的
    """
    stack = []  # 创建一个栈
    for brackets in expr:  # 迭代传过来的所有字符串
        if brackets in LEFT:  # 如果当前字符在左括号内
            stack.append(brackets)  # 把当前左括号入栈
        elif brackets in RIGHT:  # 如果是右括号
            if not stack or not 1 <= ord(brackets) - ord(stack[-1]) <= 2:
                # 如果当前栈为空，()]
                # 如果右括号减去左括号的值不是小于等于2大于等于1,目的是匹配[], (),{}
                return False  # 返回False
            stack.pop()  # 删除左括号
    return not stack  # 如果栈内没有值则返回True，否则返回False

# print match(test1)
# print match(test2)

'''
更多问题，请参考
http://python.jobbole.com/87581/
'''

'''
题目：
用一个二维数组表示一个简单的迷宫，用0表示通路，用1表示阻断，
老鼠在每个点上可以移动相邻的东南西北四个点，设计一个算法，
模拟老鼠走迷宫，找到从入口到出口的一条路径

思路：

    用一个栈来记录老鼠从入口到出口的路径
    走到某点后，将该点左边压栈，并把该点值置为1，表示走过了；
    从临近的四个点中可到达的点中任意选取一个，走到该点；
    如果在到达某点后临近的4个点都不走，说明已经走入死胡同，此时退栈，退回一步尝试其他点；
    反复执行第二、三、四步骤直到找到出口；


'''
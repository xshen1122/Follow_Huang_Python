# test_tuple.py
# coding: utf-8
'''
元组练习
1如何确定元组多大？
2. 修改元组的第一个元素
难点：元组是不可变类型，不能直接给t[0]赋值，也不能有append方法
元组不支持在原处的任何修改。
3. 复制嵌套结构，使用copy

'''
def get_tuple_size(t1):
	return len(t1)
def change_first_element(t1,number):
	t2 = ()
	t2 = (number,) + t1[1:]
	return t2



if __name__ == '__main__':
	t1 = (1,4,5)
	print get_tuple_size(t1)
	print change_first_element(t1,6)

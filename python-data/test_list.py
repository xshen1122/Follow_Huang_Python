# test_list.py
# coding:utf-8
'''
list是一种线性表，一对一的关系。

list可以放基础数据类型，也可以放OBJ

list的index和对象是一一对应的关系，找到下标，就能找到对应的对象

list可以pop和append，就是把队尾的元素弹出(意味着该元素在队列中消失），将元素插入队尾
'''
class Dog:
	def __init__(self,name):
		self.name = name

d1 = Dog('oudy')
d2 = Dog('bandian')
d3 = Dog('flash')
dog_list = []
dog_list.append(d1)
dog_list.append(d2)
dog_list.append(d3)
print dog_list # [<__main__.Dog instance at 0x0269FE40>, <__main__.Dog instance at 0x0269FE18>, <__main__.Dog instance at 0x0269FDF0>], 把狗对象放入列表
def print_dog(dog_list):
	for item in dog_list:
		print item.name
dog_list.remove(d1)
print_dog(dog_list)
dog_list.remove(d2)
print_dog(dog_list)
dog_list.pop()
print len(dog_list)
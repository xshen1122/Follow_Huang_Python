# test_list_2.py
# coding: utf-8
'''

问题：定义一个Class：包含姓名name、性别gender、年龄age，需要按年龄给学生排序。

输入：包含学生对象的List。

输出：按照年龄age进行排序好的List。

sorted(iterable, *, key=None, reverse=False)


'''
class Student:
	def __init__(self, name, gender, age):
		self.name = name
		self.gender = gender
		self.age = age
	def get_age(self):
		return self.age
	def get_name(self):
		return self.name
new_list = []
stu_list = [Student('Tom','Male',13),Student('Jerry','Male', 12), Student('Simon','Female',14)]	
new_list = sorted(stu_list, key=lambda student: student.get_age())
for item in stu_list:
	print item.get_name()
for item in new_list:
	print item.get_name()
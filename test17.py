# test17.py
# coding: utf-8
'''
练习字典的用法，将物和物联系起来

'''
person_list = []
dict1 = {'name':'tom', 'gender':'male'}
dict2 = {'name':'jean', 'gender':'female'}
dict3 = {'name':'john', 'gender':'male'}
person_list.append(dict1)
person_list.append(dict2)
person_list.append(dict3)
# print person_list
# for item in person_list:
# 	print item['name'],item['gender']
class Person:
	def __init__(self,name,gender):
		self._name = name  #不是私有的
		self._gender = gender
	def get_name_gender(self):
		return self._name, self._gender

class Sportsman(Person):
	def __init__(self,name,gender,sports):
		Person.__init__(self,name,gender)  # 如何调用父类的初始化方法？？？
		self._sports = sports
	def get_name_gender_sports(self):
		return Person.get_name_gender(self)[0],Person.get_name_gender(self)[1], self._sports

p1 = Person('john','male')
p2 = Person('jean','female')
s1 = Sportsman('fit','male','tennis')

print p1.get_name_gender()
print p1._name
print s1.get_name_gender_sports()


# test18.py
# coding: utf-8
'''
这个练习里面搞清楚类和对象


'''
class Animal(object):
	pass 
	

class Dog(Animal):
	def __init__(self,name):
		self.name = name

class Cat(Animal):
	def __init__(self,name):
		self.name = name

class Person(Animal):
	def __init__(self,name):
		self.name = name
		self.pet = None #人有一个宠物, pet是个类，是个对象，可以是猫类，也可以是狗类

class Employee(Person):
	def __init__(self,name,salary):
		super(Employee,self).__init__(name)
		self.salary = salary



class Fish(object):
	pass

class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

# rover is a dog
Oudy = Dog('Oudy')

Kafei = Cat('Kafei')

Mary = Person('Mary')
Mary.pet = Kafei

Frank = Employee('Frank',100000)
Frank.pet = Oudy
print Frank.pet.name, Frank.name, Frank.salary


flipper = Fish()
harry = Halibut()

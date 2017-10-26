# test_lintcode_easy_19.py
# coding: utf-8
'''


工厂模式是一种常见的设计模式。请实现一个玩具工厂 ToyFactory 用来产生不同的玩具类。可以假设只有猫和狗两种玩具。
样例

ToyFactory tf = ToyFactory();
Toy toy = tf.getToy('Dog');
toy.talk(); 
>> Wow

toy = tf.getToy('Cat');
toy.talk();
>> Meow



'''
# class Dog(Toy):
# 	def talk(self):
# 		print 'Wow'
# class Cat(Toy):
# 	def talk(self):
# 		print 'Meow'
class Toy:
	def __init__(self,name):
		self.name = name
	def talk(self):
		if self.name == 'Dog':
			print 'Wow'	
		elif self.name == 'Cat':
			print 'Meow'

class ToyFactory:
	
	def getToy(self,name):
		toy = Toy(name)
		return toy

if __name__ == '__main__':
	tf = ToyFactory()
	toy = tf.getToy('Cat')
	toy.talk()
	toy = tf.getToy('Dog')
	toy.talk()
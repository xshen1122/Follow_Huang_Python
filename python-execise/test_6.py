# test_6.py
# coding: utf-8
'''
餐馆：创建一个名为Restaurant的类，其方法_init_()设置两个属性：
restaurant_name和cuisine_type。
创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，
其中前者打印前述两项信息，而后者打印一条信息，指出餐馆正在营业。

'''
class Restaurant:
	def __init__(self,name,type1):
		self.restaurant_name = name
		self.cuisine_type = type1
	def describe_restaurant(self):
		print self.restaurant_name, self.cuisine_type
	def open_restaurant(self):
		print self.restaurant_name, 'is Opening!'

if __name__ == '__main__':
	r1 = Restaurant('YangDuoDuo','Dumpling')
	r1.describe_restaurant()
	r1.open_restaurant()
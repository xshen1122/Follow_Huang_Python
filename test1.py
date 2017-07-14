# test1.py
# coding: utf-8
# print globals()
# for g, d in globals().items():
# 	print g, d



# import traceback
# try:
#     1/0
# except Exception,e:
#     traceback.print_exc()

# apply 函数

# def fun(a,b):
# 	print a,b
# def say():
# 	print 'hello'

# apply(fun,('crunchy','frog'))
# apply(fun,(), {'a': 'crunchy', 'b':'frog'})
# apply(fun, ('crunchy',),{'b':'frog'})


# apply 函数的应用，调用基类的构造函数
class Rectagle:
	def __init__(self,color='white', width=10,length=10):
		print 'Create a' +str(self) + '颜色为' + color + '宽度为' + str(width) + '长度为' +str(length)
class RoundRectagle(Rectagle):
	# pass #这里直接继承也行啊。
	def __init__(self,**kwargs):#怎么传**kwargs
		apply(Rectagle.__init__,(self,),kwargs)


if __name__ == '__main__':
	my = Rectagle('black',20,20)
	# my = RoundRectagle('green',30,30) #怎么传**args？？？
	round = RoundRectagle(color='green',width=30,length=30)
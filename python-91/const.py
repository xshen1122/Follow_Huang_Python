# const.py
# coding: utf-8
'''

通过自定义类实现常量功能。
这要求符合“命名全部为大写”和“值一旦被绑定便不可再修改”这两个条件。
'''
import sys

class const:
  class ConstError(TypeError): pass
  class ConstCaseError(ConstError): pass

  def __setattr__(self, name, value): # use . command.
  	print 'run here'
  	if name in self.__dict__:
  		raise self.ConstError("can't change const %s" % name)
  	if not name.isupper():
  		raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
  	self.__dict__[name] = value

if __name__ == '__main__':
	
	test = const() #直接使用网页上提到的方法直接掉，根本不会进入const类。
				   #必须要创建实例，然后再调，才行。
	print test
	test.NAME = 'name'
	print test.NAME
	test.NAME = 'name1'
	print test.NAME
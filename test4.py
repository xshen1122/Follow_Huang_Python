# test4.py
# coding: utf-8
'''
动态调用	


'''
# import glob, os
# modules = []
# print glob.glob('*-plugin.py')
# for module_file in glob.glob('*-plugin.py'):
# 	print module_file
# 	try:
# 		module_name, ext = os.path.splitext(os.path.basename(module_file))
# 		module = __import__(module_name)
# 		modues.append(module)
# 	except ImportError:
# 		pass
# print len(modules)
# for module in modules:
# 	print module

# 	#没看懂__import__一系列的例子。。。。


def dump(value):
	print value , '--->', dir(value)


import sys
# dump(0) # number
'''
0 ---> ['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']

'''
# dump('hello') # string

# dump(0.0j)
dump(len)  # function
dump(list)
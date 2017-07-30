# test_args.py
# coding: utf-8
'''
test *args, **args
*args = tuple
**args = dict
args is changed to values
'''

def test(*args):
	print args
def test1(*value):
	print value
def test2(**args):
	print args

if __name__ == '__main__':
	test(1,2,3)
	test('a','b','c')
	test1(3,4)
	test2(a=1,b=2)
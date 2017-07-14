# test2.py
'''
test *args, **kwargs
'''
def fun(*args, **kwargs):
	print 'args=',args
	print 'kwargs = ', kwargs

fun(1,2)
fun(a=1,b=2,c=3)
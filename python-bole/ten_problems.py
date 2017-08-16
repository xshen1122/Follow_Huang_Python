# ten_problems.py
# coding: utf-8
'''
（一）、如何反序的迭代一个序列？
如何用Python来进行查询和替换一个文本字符串？
（三）、使用Python
（四）、重新实现str.strip()，注意不能使用string.*strip()
（五）、 阅读下面的代码，它的输出结果是什么？（super）
（六）、Python的函数参数传递
（七）、类变量和实例变量，通过类.变量和实例.变量来调用
（八）、Python在函数式编程方面的支持。
（九）、 以下代码将输出什么？（考察list）
（十）、 以下代码将输出什么？（考察）


'''
def test_fun():
	temp = [lambda x: i*x for i in range(4)]
	return temp
for everyLambda in test_fun():
	print everyLambda(2)
'''
为啥结果为6？
这个原因是Python的闭包的后期绑定导致的late binding。
这意味着在闭包中的变量是在内部函数被调用的时候被查找。
所以结果是，当任何的testFun()返回的函数被调用，在那时，
i的值是在它被调用时的周围作用域中查找，到那时，
无论哪个返回的函数被调用，for循环已经完成，i的最后值是3，因此每个返回的函数testFun的值都是3。
'''
'''
map(func, seq), 将列表中的每个元素都用func计算一遍，然后输出结果列表
filter

'''
print filter(lambda x: x%2==0, range(0,10))#找出0-9的偶数
print map(lambda x:x**2, [3,6,9,12,15,18])#返回0-9的平方
#在map的seq中嵌套数组是不行的。但是可以添加多个数组,代表将seq1和seq2的数字进行相加输出结果数组
print map(lambda x, y : x+y, [3,6,9],[1,3,5])
print map(lambda x, y, z: x+y+z, [1,2,3],[4,5,6],[7,8,9]) #可以扩展为N个数组，但数组个数要一致

# reduce比map要复杂，他是一个迭代的过程，把前两个的结果作为参数输入下一次运算
print reduce(lambda x,y: x+y, range(0,10))#返回0=1+2+....+9
print reduce(lambda x,y: x+y, range(0,10),100)
print reduce(lambda x,y: x+1+y, range(0,10))# 从这里看出，lambda表达式必须是2个变量，因为会放入seq[0],seq[1]

'''
filter是过滤序列，和map有点类似，但只返回false，true
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的时，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素

练习： 请尝试用filter()删除1~100的素数。通过返回的True，False来筛选列表的值，返回的仍然是列表
'''

def is_susu(number):
	for i in range(2,number):
		if number % i == 0:
			return False
	return True
print filter(is_susu, range(1,100))
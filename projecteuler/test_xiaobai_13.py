# test_xiaobai_13.py
# coding: utf-8
'''
Work out the first ten digits of the sum of the following 
one-hundred 50-digit numbers.
这道题比较有意思，有100个50位的整数。需要求出这些数的和，但只显示前10位
50位整数相加，应该处理不了这么大的整数。python可以处理50位以上的整数。
那python处理整数的极限？
Python int有多种数字类型：整型int、长整型、布尔型bool、浮点数float、复数complex

from baidu:
python支持大数计算，无限位数。
对于小整数，它会使用机器自身的整数计算功能去快速计算，
当超出机器自身所能支持的范围的时候，自动转换大数计算。
1. 先把整数读取到list中。
2. 将所有100个数字相加
3. 转化成为str，取出前面10个字符
4. 该题的关键是python支持任意大的整数，不然肯定要考虑50位怎么存放。

'''
def readNumber(filename):
	myfile=open(filename,'r')
	number_list = []
	for line in myfile.readlines():
		number_list.append(long(line))
	return number_list



if __name__ == '__main__':
	filename = '50digits.txt'
	number_list = readNumber(filename)
	result = 0
	for item in number_list:
		result += item
	print (str(result))[:10]
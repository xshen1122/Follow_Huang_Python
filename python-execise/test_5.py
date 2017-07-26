# test_5.py
# coding: utf-8
'''

打印99乘法表， 或者可以扩展为12*12， 主要是循环的应用
'''
def print_multiple(k):
	line = 'x'
	for i in range(0,k+1):
		for j in range(0,k+1):
			if i == 0 or j==0:
				line += str((i+1)*(j)) + '\t'
			# line += str(i)+'*'+str(j) + '\t'
			else:
				line += str(i*j) + '\t'
		print line + '\n'
		line = 'x'

if __name__ == '__main__':
	print_multiple(12)
# tips_03.py
# coding:utf-8
'''
有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中

'''

with open('A.txt','r') as file1:
	for line in file1.readlines():
		line1=line
with open('B.txt','r') as file2:
	for line in file2.readlines():
		line2=line
line3=line1+line2

with open('C.txt','w') as file3:
	for item in sorted(line3):
		file3.write(item)

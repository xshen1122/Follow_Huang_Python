# test11.py
# coding: utf-8
import fileinput
# import sys
# import glob
# # for line in fileinput.input('test9.py'):
# # 	sys.stdout.write('----->')
# # 	sys.stdout.write(line)
# for line in fileinput.input(glob.glob('*.py')): # 把当前目录下的所有文件都显示出来
# 	if fileinput.isfirstline():
# 		sys.stdout.write('This is the first line')
# 	sys.stdout.write(line)

'''
使用shutil来复制文件夹

'''
# import shutil
# import os

# for file in os.listdir('.'):
# 	if os.path.splitext(file)[1] == '.py':
# 		print file
# 		shutil.copy(file,file+'backup')

'''
mktemp()
创建临时文件
'''
import tempfile
import os
temp_file = tempfile.mktemp()
print temp_file
file = open(temp_file,'w+')
file.write('*'*1000)
file.seek(0)
print len(file.read()), 'Bytes'
file.close
try:
	os.remove(temp_file)
except OSError:
	pass
file_1 = tempfile.TemporaryFile() #建立一个临时文件，连文件名都没有，file_1.close()就删除
for i in range(1000):
	file_1.write('*'*i)
file_1.close()
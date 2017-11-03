# analysis_log.py
# coding: utf-8
'''
Input: xxx.log
1. make sure no error - ( 0 onError, total onComplete = total files)
2. make sure no crash (if we have total 83 files means no crash)
3. ?? other criteria??


'''
import os
def checkKeywords(filename):
	error_result = 0
	complete_result = 0
	with open(filename,'r') as myfile:
		for line in myfile.readlines():
			if 'onError' in line:
				error_result +=1
			if 'onCompletion' in line:
				complete_result += 1
	if error_result == 0 and complete_result == 1:
		
		return True
	else:
		
		return False

folderPath = '/home/real/Videos/Log/1103/'
file_list = os.listdir(folderPath)
if len(file_list) == 83:
	print 'All Test Cases are executed!'
else:
	print 'Not all Test Cases are executed!'

for filename in file_list:
	
	if checkKeywords(folderPath + filename):
		print filename + '--Pass'
	else:
		print filename + '--Fail'


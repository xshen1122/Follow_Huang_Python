# test_find_top3_size.py
# coding: utf-8
import os
GIVE_DIR='/home/real/Documents/python/math'

def processTop3Size(dirname):
	
	filename_list = []
	filesize_list = []
	for item in os.listdir(dirname):
		filename_list.append(item)
		filesize_list.append(os.stat(item).st_size)

	return dict(zip(filename_list,filesize_list))

if __name__ == '__main__':
	file_dir = {}
	sorted_list = []
	file_dir = processTop3Size(GIVE_DIR)
	sorted_list = sorted(file_dir.items(), key=lambda d: d[1],reverse=True)

	print sorted_list[0],sorted_list[1],sorted_list[2]
	# print sorted(file_dir.values(),key = lambda d:d) # not good, no filename information


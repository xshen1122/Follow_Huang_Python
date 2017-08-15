# process_onSeekComplete_onLoadingStateUpdate.py
# coding: utf-8
import re
def get_time(line):
	mytime = line[6:18]
	hour = mytime[:2]
	minute = mytime[3:5]
	second = mytime[6:8]
	return int(hour)*3600 + int(minute) * 60 + int(second)


myfile = open(r'C:\Users\real-qa\_0801\out1\111.log', 'r')
my_list = []
flag = False
start_time = []
end_time = []
for line in myfile:
	if 'SPCLog  : RMHDPlayer.onSeekComplete.' in line:
		my_list.append(line)
		start_time.append(get_time(line))
		flag = True
	if 'SDL     : onLoadingStateUpdate' in line and flag:
		my_list.append(line)
		end_time.append(get_time(line))
		flag = False
myfile.close()
result = 0
for i in range(len(start_time)):
	result += end_time[i] - start_time[i]
	print end_time[i] - start_time[i]
print float(result/len(start_time))

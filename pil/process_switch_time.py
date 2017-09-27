# process_switch_time.py
# coding: utf-8
'''
Request: less than 10 seconds during manual switch
09-12 15:57:59.170 28356 28356 D SPCLog  : SwitchingState:0,0
09-12 15:58:02.699 28356 28356 D SPCLog  : SwitchingState:1,2000000
09-12 15:58:08.981 28356 28356 D SPCLog  : SwitchingState:0,0
09-12 15:58:16.458 28356 28356 D SPCLog  : SwitchingState:1,4000000



'''
def get_seconds(timestring):
	hh = int(timestring.split(':')[0])
	mm = int(timestring.split(':')[1])
	ss = float(timestring.split(':')[2])
	return hh*3600+mm*60+ss


filedir = '/home/real/log/_0914/'
myfile = open(filedir + '4.log','r')
end_time = []
start_time = []
for line in myfile:
	if 'SwitchingState:0,0' in line:
		start_time.append(get_seconds(line.split()[1]))
	if 'SwitchingState:1' in line:
		end_time.append(get_seconds(line.split()[1]))


myfile.close()
interval_time=[]
for i in range(len(start_time)):
	print 'the ',i,' times is', end_time[i]-start_time[i]
	interval_time.append(end_time[i]-start_time[i])
flag_15=0
flag_10_15=0
for item in interval_time:
	if item -10.0 > 0 and item -15.0 < 0:
		print item
		flag_10_15 = flag_10_15 + 1
	elif item - 15.0 > 0:
		flag_15 += 1
print flag_15
print flag_10_15
print 'Larger than 10', float(flag_10_15)/float(len(start_time))*100
print 'Larger than 15',float(flag_15)/float(len(start_time))*100
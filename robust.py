# robust.py
# coding:utf-8
'''
generate contents from txt by realproducerhd

'''
def processBitrate(resolution):
	width = resolution.split('x')[0]
	if int(width) <= 240:
		return '350k','64k'
	elif int(width) <= 480:
		return '500k','128k'
	elif int(width) <= 720:
		return '1000k','128k'
	elif int(width) <= 1080:
		return '2000k','128k'
	else:
		return '4000k','128k'
content_list = []
filename = 'xmen_2560x1440_60sec.mp4'
with open('88.txt','r') as myfile:
	for line in myfile.readlines():
		if 'resolution' in line and 'm3u8' not in line:
			content_list.append(line[:-1].split('_'))
print len(content_list)
print content_list
with open('88.sh','w') as newfile:
	for item in content_list:
		str1 = ''

		outputfile = item[0] + '_' + item[1]+'_'+item[2] +'.' + item[2]
		str1 += './realproducerhd -i ' + filename + ' -s ' + item[1] + ' -avgrate ' + processBitrate(item[1])[0] + ' -b:a ' + processBitrate(item[1])[1] + ' ' + outputfile
		newfile.write(str1+'\n')




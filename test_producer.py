# test_producer.py
# coding: utf-8
'''
create scripts
'''
myfile = open('lavra.sh','w')
myfile.write('#!/bin/bash'+'\n')

for i in range(1,100):
	if i in range(1,10):
		str1 = './realproducerhd -i lavra/0' + str(i) +'.mp4 -s 1280x720 -avgrate 1.5M  rmhd/0' + str(i) +'.rmhd'
	else:
		str1 = './realproducerhd -i lavra/' + str(i) +'.mp4 -s 1280x720 -avgrate 1.5M  rmhd/' + str(i) +'.rmhd'
	myfile.write(str1+'\n')
myfile.close()

# test_producer_1.py
# coding: utf-8
myfile = open('lavra1.sh','w')
myfile.write('#!/bin/bash'+'\n')

for i in range(1,53):
	if i in range(1,10):
		str1 = './realproducerhd -i lavra/0' + str(i) +'.flv -s 1104x622 -avgrate 1M  rmhd/0' + str(i) +'.rmhd'
	else:
		str1 = './realproducerhd -i lavra/' + str(i) +'.flv -s 1104x622 -avgrate 1M  rmhd/' + str(i) +'.rmhd'
	myfile.write(str1+'\n')
myfile.close()
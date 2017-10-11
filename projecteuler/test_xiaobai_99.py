# test_xiaobai_99.py
# coding: utf-8
'''
However, confirming that 632382 518061 > 519432 525806 would be much more difficult, as both numbers contain over three million digits.

'''
import math
def compareNumber(l1,l2):
	n1 = l1[0]**l1[1]
	n2 = l2[0]**l2[1]


	if math.log(n1) > math.log(n2):
		print l1[0], '**', l1[1], '>', l2[0], '**', l2[1]
	else:
		print l1[0], '**', l1[1], '<', l2[0], '**', l2[1]
def processList(yourlist):
	new_list = []
	for i in range(len(yourlist)):
		new_list.append([int(yourlist[i][0]),int(yourlist[i][1][:-1])])

	return new_list

if __name__ == '__main__':
	number_list = []
	n1_list = []
	n2_list = []
	myfile = open('p099_base_exp.txt','r')
	for line in myfile.readlines():
		number_list.append(line.split(','))

	
	for i in range(len(number_list)):
		if i%2 == 0:
			n1_list.append(number_list[i])
		else:
			n2_list.append(number_list[i])
	
	new_list1 = processList(n1_list)
	new_list2 = processList(n2_list)
	for i in range(len(new_list1)):
		compareNumber(new_list1[i], new_list2[i])


	myfile.close()
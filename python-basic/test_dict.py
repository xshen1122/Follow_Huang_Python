# test_dict.py
# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
'''
UP is very important:
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

read out 北 京101010100朝阳101010300顺义101010400怀柔101010500通州101010600昌平
101010700延庆 101010800丰台101010900石景山101011000大兴101011100房山
101011200密云101011300门头沟 101011400平谷101011500八达岭101011600佛爷顶
101011700汤河口101011800密云上甸子101011900斋堂 101012000霞云岭101012100北京
城区101012200 and save them into dict  

dict1['朝阳'] = 10xxx

'''
str1 ="北京101010100朝阳101010300顺义101010400怀柔101010500通州101010600昌平101010700延庆 101010800丰台101010900石景山101011000大兴101011100房山101011200密云101011300门头沟 101011400平谷101011500八达岭101011600佛爷顶101011700汤河口101011800密云上甸子101011900斋堂 101012000霞云岭101012100北京城区101012200"

def seperate(str1):
	# str1.decode('utf-8')
	number=''
	place=''
	number_list =[]
	place_list = []
	new_list = []
	for item in str1:
		if item.isdigit():
			if place != '':
				place_list.append(place)
			place=''
			number += item
		else:
			if number != '':
				number_list.append(number)
			number = ''
			place += item
	
	post_dict =dict(zip(place_list, number_list))
	return post_dict


if __name__ == '__main__':
	# print str1
	post_dict = seperate(str1)
	for item in post_dict.keys():
		print item, post_dict[item]
	

	

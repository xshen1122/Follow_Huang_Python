# test13.py
# coding: utf-8
'''
比如列表[0,0,0,1,1,2,3,3,3,2,3,3,0,0]分割成[0,0,0],[1,1],[2],[3,3,3],[2],[3,3],[0,0]

'''

'''
思路：
1. 取出第一组相同元素，返回相同元素组成的数组，和pos
2. 去掉第一组元素，从pos开始 yourlist[pos:]
3. 循环取出第一组相同元素，直到len(yourlist)>1 (还有数组)

'''
def parse_list(yourlist):
	result_list = []
	def get_first_list(yourlist):
		new_list = []
		
		for i in range(0,len(yourlist)):
			
			if yourlist[i] == yourlist[0]:
				new_list.append(yourlist[i])
			else:
				return new_list, i
		return new_list,i
	pos=1
	while not pos==0:
		result,pos= get_first_list(yourlist)
		result_list.append(result)
		
		yourlist = yourlist[pos:]

	if result_list[-1]==[0]:
		return result_list[:-1]
	else:
		return result_list
	
'''
最后连续2个相同元素的还需要再调下。思路不太清楚了。
'''


def test_parse_list():
	yourlist = [0,0,0,1,1,2,3,3,3,2,3,3,0,0,5]
	print parse_list(yourlist)


if __name__ == '__main__':
	test_parse_list()
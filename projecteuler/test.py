# test.py
# coding: utf-8
def reverse(data):
	for i in range(len(data)):
		for j in range(i+1, len(data)):
			temp=data[i][j]
			data[i][j]=data[j][i]
			data[j][i]=temp
	return data


	        
	


if __name__ == '__main__':

	list1 = [[1,2,3],[4,5,6],[7,8,9]]
	final_list = []
	print reverse(list1)
	for i in range(3):
		temp_list = []
		for j in range(3-i):
			temp_list.append(list1[i+j][i+j])
		if len(temp_list) >=2:
			final_list.append(temp_list)
	print final_list
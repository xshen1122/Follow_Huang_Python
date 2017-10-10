# test_xiaobai_39.py
# coding: utf-8
'''


If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

a+b+c=120 - p - find a,b,c
a*a + b*b = c*c
'''
def inclusive(a,yourlist):
	for item in yourlist:
		if a in item:
			return False
	return True
def findABC(p):
	result_list = []

	for a in range(1,p):
		for b in range(1,p):
			if a*a + b*b == (p-a-b)*(p-a-b) and inclusive(a,result_list) and inclusive(b,result_list):

				
				result_list.append([a,b,p-a-b])




	return result_list

if __name__ == '__main__':
	result_dict ={}
	for number in range(121,1001):
		result= findABC(number)
		result_dict.setdefault(len(result),result)

	print result_dict
'''
OUTPUT:
p=840, has 8 triangle numbers:

8: [[40, 399, 401], [56, 390, 394], [105, 360, 375], [120, 350, 370], [140, 336, 364], [168, 315, 357], [210, 280, 350], [240, 252, 348]]}


'''



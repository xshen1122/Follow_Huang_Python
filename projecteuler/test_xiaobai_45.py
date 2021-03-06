# test_xiaobai_45.py
# coding: utf-8
'''


Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.


'''
def getTriangle(n):
	return n*(n+1)/2
def getPentagonal(n):
	return n*(3*n-1)/2
def getHexagonal(n):
	return n*(2*n-1)
t_dict={}
p_dict={}
h_dict={}
for i in range(286,100000):
	t_dict.setdefault(getTriangle(i),i)
for i in range(166,100000):
	p_dict.setdefault(getPentagonal(i),i)
for i in range(144,100000):
	h_dict.setdefault(getHexagonal(i),i)
item = 40756
for item in t_dict.keys():
	if item in p_dict.keys() and item in h_dict.keys():
		print 'find it', item
		break

	print item, 'times'
print t_dict[item], p_dict[item],h_dict[item]

'''
OUTPUT
find it 1533776805
55385 31977 27693


'''
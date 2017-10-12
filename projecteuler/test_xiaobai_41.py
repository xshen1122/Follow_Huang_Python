# test_xiaobai_41.py
# coding: utf-8
'''


We shall say that an n-digit number is pandigital if it makes use of 
all the digits 1 to n exactly once. For example, 2143 is a 4-digit 
pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?


'''
def checkPrime(number):
	for i in range(2,number):
		if number%i == 0:
			return False
	return True
def checkNumber(number):
	n_list = []
	for item in str(number):
		n_list.append(item)
	if len(n_list) == len(set(n_list)):
		return True
	else:
		return False
if __name__ == '__main__':
	number = 987654321
	for number in range(987654321,1000,-1):
		print number
		if not checkNumber(number):
			pass
		else:
			if checkPrime(number):
				print 'the largest pandigital prime is ', number
				break
			else:
				pass

# test_xiaobai_3.py
# coding:utf-8
'''


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

1. max prime factor.
2. 600851475143 too big.-> Memory Error
3. 质因数分解
'''

def findMaxPrime(number):
	max_one = 1
	i = 2
	while i< number:
		if number%i == 0:
			return i
		i += 1
	return 0

if __name__ == '__main__':
	value = 600851475143
	# value = 13195

	while findMaxPrime(value) != 0:
		
		value = value/findMaxPrime(value)
		
	print value
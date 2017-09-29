# test_xiaobai_14.py
# coding: utf-8
'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
 Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

100万以下的数，谁有最长的链条？
1. 遍历法，记下链条（字符串），但不需要从最小的数开始。
2. 从90万到100万，是93万 ， 507次转换
3. 从10万到100万，是80多万，有525次转换

'''
def getCollatz(number):
	chain_str = ''
	chain_str += str(number) + '-->'
	chain_list = []
	chain_list.append(number)
	while number != 1:
		if number % 2 == 0:
			number = number/2
			chain_str += str(number) + '-->'
			chain_list.append(number)
		else:
			number = 3*number+1
			chain_str += str(number) + '-->'
			chain_list.append(number)
	return [chain_str[:-3],len(chain_list)]

if __name__ == '__main__':
	chain_dict = {}
	temp_list = []
	for i in range(100000,900000):
		temp_list = getCollatz(i)
		chain_dict.setdefault(temp_list[0],temp_list[1])

	print sorted(chain_dict.items(), key=lambda d: d[1],reverse=True)[0]
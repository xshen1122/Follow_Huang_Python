# test_xiaobai_38.py
# coding: utf-8
'''


Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

9 digits
[999999999,999999998] x, [1,2,3,4]
1 digit - [1,2,3,4,5]
2 digit - [1,2,3,4,5??],[1,2,3,4??]
first digit should be 9
'''
total_str = ''
int_list = []
for i in range(1,6):
	result = 9*i
	total_str += str(result)
int_list.append(int(total_str))
total_str = ''
for i in range(1,4):
	result = 391 * i
	total_str += str(result)
int_list.append(int(total_str))

print int_list

'''
OUTPUT:
918273645 should be max.

'''
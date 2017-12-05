# test_copy.py
# coding: utf-8
'''
copy and deepcopy
'''

import copy
list1 =[[1,2,3],[4,5,6],[7,8,9]]
l2 = copy.copy(list1)
l3 = copy.deepcopy(list1)

print 'list1 element 0 is ', id(list1[0])
print 'list2 element 0 is ', id(l2[0])
print 'list3 element 0 is ', id(l3[0])
'''
OUTPUT
list1 element 0 is  140392925515288
list2 element 0 is  140392925515288
list3 element 0 is  140392925662168

'''

list1[0][0]=100

print list1
print l2
print l3
'''
OUTPUT:
[[100, 2, 3], [4, 5, 6], [7, 8, 9]]
[[100, 2, 3], [4, 5, 6], [7, 8, 9]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]



'''
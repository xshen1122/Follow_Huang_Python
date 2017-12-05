# test_operator_1.py
# coding: utf-8
'''
operator.itemgetter()


'''
import operator
list1 = [1,2,3]
b= operator.itemgetter(1) # get the postion = 1 value.
print b(list1)
# <operator.itemgetter object at 0x7f9f1429d790>
print type(operator.itemgetter(1))


dict1 = {'a':10, 'b':12, 'c':20, 'd':9}
print sorted(dict1.items(), key=operator.itemgetter(1),reverse=True)
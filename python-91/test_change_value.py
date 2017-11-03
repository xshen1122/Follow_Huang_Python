# test_change_value.py
# coding: utf-8
'''

Not recommand using tmp value when change 2 values.
'''
x = 10
y =20
x, y = y,x # simple usage
print 'x is ', x , 'y is ', y
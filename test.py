# test.py
# coding: utf-8
import os
filepath = 'C:\@z-python_examples'
if not os.path.exists(filepath):
	raise Exception(filepath + 'NOT existing')
for item1, item2, item3 in os.walk(filepath):
	print item1, item2, item3
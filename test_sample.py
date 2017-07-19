# test_sample.py
# coding: utf-8
def add_one(x):
	return x+1
def add_two(x):
	return x+2

def test_answer():
	assert add_one(3) == 4

def test_01():
	assert add_two(4) == 6
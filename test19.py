# test19.py
# coding: utf-8
'''
用来练习py.test怎么用
先建立简单的函数

'''
import pytest

def test_main():
	assert 5!=5
if __name__ == '__main__':
	pytest.main()
# test_main.py
# coding:utf-8
import pytest
def test_main():
	assert 5==5
if __name__ == '__main__':
	pytest.main()
	# pytest.main('目录') 指定目录下的所有test_开头的py文件
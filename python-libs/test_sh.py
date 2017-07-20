# test_sh.py
# coding: utf-8
from sh import ifconfig
print(ifconfig("wlan0"))

'''
ImportError: sh 1.12.14 is currently only supported on linux and osx. 
please install pbs 0.110 (http://pypi.python.org/pypi/pbs) for windows support.

'''
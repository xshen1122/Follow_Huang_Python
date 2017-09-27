# test_subprocess.py
# coding: utf-8
'''

How to use subprocess module?

'''
import subprocess

subprocess.call("ls")

'''
output is listed all files/dirs under current folder
test_1.py
test_2.py
test_3.py
test_subprocess.py
'''


subprocess.call( [ "cat","test_subprocess.py"] )
# output the content of the files

subprocess.call(["/home/real/0821/producer_release/ffprobe 1080p-5M.rmhd"])
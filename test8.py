# test8.py
# coding: utf-8
import os
import sys
program = 'python'
arguments = ['hello.py']
print os.execvp(program, (program,) + tuple(arguments))
print 'goodbye'
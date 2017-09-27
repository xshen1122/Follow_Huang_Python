# b.py
# coding: utf-8
import gl 

def modifyConstant():
	global CONSTANT 
	CONSTANT = 0
	print CONSTANT
	CONSTANT +=1
	return CONSTANT

if __name__ == '__main__' : 
    modifyConstant() 
    print CONSTANT
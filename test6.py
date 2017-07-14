# test6.py
# coding: utf-8
NAME = "script.py"
BODY = """prnt 'owl-scrunching time'"""

try:
	compile(BODY,NAME,"exec") 
except SyntaxError,v:
	print 'SyntaxError', v, 'in', NAME 


BODY = """print 'The ant, the instroduction'   """
code = compile(BODY,'<script>',"exec")
print code
exec(code)
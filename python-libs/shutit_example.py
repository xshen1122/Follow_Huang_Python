# shutit_example.py
# coding: utf-8
import shutit  
session = shutit.create_session('bash')  
session.send('echo Hello World', echo=True)

'''
1. shutit模块缺少termios
2. 网友说：termios for unix


'''
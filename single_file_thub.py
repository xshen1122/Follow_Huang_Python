# single_file_thub.py
# coding: utf-8
import time
from subprocess import Popen
for j in range(99999):
	for i in range(300):
		cmd = ['adb', 'shell', 'mv', r'/sdcard/test/%s.wmv' % (str(i),), r'/sdcard/test/%s.wmv' % (str(i+1),),]
		Popen(cmd).wait()
		cmd = ['adb', 'shell', 'am', 'broadcast', '-a', 'android.intent.action.MEDIA_MOUNTED', '-d', r'file:///mnt/sdcard/test/',]
		Popen(cmd).wait()
	cmd = ['adb', 'shell', 'mv', r'/sdcard/test/*.wmv', r'/sdcard/test/0.wmv' ,]
	Popen(cmd).wait()
	time.sleep(30)
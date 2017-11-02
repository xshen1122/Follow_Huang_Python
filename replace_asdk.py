# replace_asdk.py
# coding: utf-8
'''
1. copy 70 to newstreaming
2. copy 484 to asdk
>>> import os
>>> os.system("cp -rf /copyfolder /home/user/folder")
'''
import os 
import os.path 
import shutil 
import sys

for i in range(len(sys.argv)):
	print sys.argv[i]

# 1 means ASDK
# 2 means RMXD
def checkFiles(f1):
	if os.path.exists(f1):
		print f1 , 'Exist'
		return True
	else:
		print f1, 'Not Exist'
		return False






def copyASDK():
	ASDK_PATH='/home/real/SW/' + sys.argv[2]
	print ASDK_PATH
	asdkJar = ASDK_PATH+ '/libs/rmhd_android_sdk.jar'
	asdkSo = ASDK_PATH +'/src/main/jniLibs/armeabi-v7a'
	AS_LIB= '/home/real/1017/Rmhd_Android_SDK_Test/AndroidTestAutomation/app/libs/'
	AS_SO = '/home/real/1017/Rmhd_Android_SDK_Test/AndroidTestAutomation/app/src/main/jniLibs/'
	os.system('rm -r '+AS_SO +'/*')
	if checkFiles(asdkJar) and checkFiles(asdkSo):
			# copy Jar to AS
		c1 = 'cp ' +asdkJar + ' ' + AS_LIB
		os.system(c1)

		# copy So dir to AS
		c2 = 'cp -rf ' +  asdkSo + ' ' + AS_SO
		os.system(c2)
	print c1
	print c2
	
def copyRMXD():
	RMXD_PATH='/home/real/SW/' + sys.argv[2]
	rmxdJar = RMXD_PATH+'/app/libs/rmxdplayer.jar'
	rmxdSo = RMXD_PATH +'/app/src/main/libs/armeabi'
	AS_LIB= '/home/real/1017/Rmhd_Android_SDK_Test/AndroidTestAutomation/app/libs/'  
	AS_SO = '/home/real/1017/Rmhd_Android_SDK_Test/AndroidTestAutomation/app/src/main/jniLibs/'
 	os.system('rm -r '+AS_SO +'/*')
 	if checkFiles(rmxdJar) and checkFiles(rmxdSo):
 			# copy RMXD Jar to AS
		c3 = 'cp ' + rmxdJar + ' ' + AS_LIB
		os.system(c3)

		# copy RMXD So dir to AS
		c4 = 'cp -rf ' +  rmxdSo + ' ' + AS_SO
		os.system(c4)
	print c3
	print c4


if __name__ == '__main__':
	if sys.argv[1] == 'asdk':
		copyASDK()
	if sys.argv[1] == 'rmxd':
		copyRMXD()	







#check all jar and folder are existing:









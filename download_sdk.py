# download_sdk.py
# coding:utf-8
'''

http download asdk .gz files and unzip to ### build

input build_id
HTTP 403命令是禁止恶意访问此网站,不能从此网站中抓取内容
'''
import sys
import httplib2
build_id=sys.argv[2]
url = 'http://10.10.49.50:8080/view/GrailPlayer/job/GrailPlayer_android/' + build_id +'/artifact/app.binaries.tgz'
filename = '/home/real/SW/'+'app.binaries.tgz'
h = httplib2.Http()  
resp, content = h.request(url)  
print resp['status']
if resp['status'] == '200':
	print 'here'
	with open(filename, 'wb') as f:  
		f.write(content)  
print 'download complete'
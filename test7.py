# test7.
# coding: utf-8
class HTTPError(Exception):
	def __init__(self,url,errcode,errmsg):
		self.url= url
		self.errcode = errcode
		self.errmsg = errmsg

	def __str__(self):
		return'HTTPError for %s: %s,%s' % (self.url, self.errcode, self.errmsg)

http = HTTPError('www.python.org','404','not reachable')
print http
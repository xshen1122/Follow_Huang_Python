# app.py
# coding: utf-8

import web
urls = ('/','index')
app = web.application(urls, globals())

render = web.template.render('templates/') # 作者没说，一定要在python bin/app.py,否则找不到templates路径。或者给出templates的绝对路径
class index:
	def GET(self):
		greeting = 'Hello World'
		return render.index(greeting = greeting)
		# return greeting


if __name__ == '__main__':
	app.run()

# 运行 python app.py
# 在浏览器中输入localhost:8080
# 浏览器的BODY部分会显示 Hello World
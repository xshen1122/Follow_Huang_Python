# bs4_example.py
# coding: utf-8
'''
1. 实验下BeautifulSoap4如何用？



'''
from bs4 import BeautifulSoup  
import pdir
# 创建一个html 字符串，用三个双引号括起来，可以让字符串分段
html_doc = """ 
<html><head><title>The Dormouse's story</title></head> 
<body> 
<p class="title"><b>The Dormouse's story</b></p> 
 
<p class="story">Once upon a time there were three little sisters; and their names were 
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, 
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
and they lived at the bottom of a well.</p> 
 
<p class="story">...</p> 
""" 
#初始化 soup对象
soup = BeautifulSoup(html_doc,'lxml')  

print soup.title
# print pdir(soup) # 查看soup对象有哪些属性和方法
# print soup.title.parent
# print soup.title.parent.parent
print soup.title.name
print soup.p
print soup.p['class']
print soup.a
print soup.find_all('a')
for link in soup.find_all('a'):  
    print(link.get('href')) 

print(soup.getText())  

print('all tags : <<<<<<')  
for tag in soup.find_all(True):  
    print(tag.name)  

    
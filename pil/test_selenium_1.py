# test_selenium_1.py
# coding: utf-8
from selenium import webdriver  
  
# driver = webdriver.Chrome()  
driver = webdriver.Firefox()  
driver.get('http://www.baidu.com')  
print driver.title  
driver.quit() 
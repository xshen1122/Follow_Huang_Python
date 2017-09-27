# test_csv.py
# coding: utf-8
import csv

csvfile = open('1.csv')#打开一个文件
csvReader = csv.reader(csvfile)#返回的可迭代类型
print(type(csvReader))
for content in csvReader:
  print(content)
csvfile.close()#关闭文件

'''
#读取csv文件方法2
import csv
with open('csvWtite.csv',newline='') as csvfile:#此方法:当文件不用时会自动关闭文件
  csvReader = csv.reader(csvfile)
  for content in csvReader:
    print(content)
'''

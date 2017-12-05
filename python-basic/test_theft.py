# test_theft.py
# coding: utf-8
'''
抓了a,b,c,d4名犯罪嫌疑人.其中有一名是小偷,审讯中:
        a说我不是小偷
        b说c是小偷
        c说小偷肯定是d
       d说c胡说!
其中有3个人说的是实话,一个人说的是假话,编程推断谁是小偷。


'''
theft = ['a','b','c','d']
for item in theft:
	summary = (item!='a') + (item == 'c') + (item == 'd') + (item !='d')
	if summary == 3:
		print 'theft is' + item
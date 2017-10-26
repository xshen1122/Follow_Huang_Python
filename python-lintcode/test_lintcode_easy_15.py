# test_lintcode_easy_15.py
# coding: utf-8
'''


We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
样例

n = 10, I pick 4 (but you don't know)

Return 4. Correct !


猜数字用class的实现更好，因为可以将猜数字的次数放在成员变量里进行保存。当然也可以保存其他的数据。
'''
class GuessNumber:
	def __init__(self,original):
		self.value = original
		self.times = 0


	def guessNumber(self,yournumber):
		self.times +=1
		if int(yournumber) < self.value:
			
			print 'Wrong, the number is bigger than', yournumber
			return 1
		elif int(yournumber) >self.value:
			
			print 'Wrong, the number is smaller than',yournumber
			return -1
		else:

			print 'Correct!'
			return 0


if __name__ == '__main__':
	test=GuessNumber(10)
	print test.value
	while True:
		yournumber = raw_input('Please input your guess N')
		if test.guessNumber(yournumber) == 0:
			break
	print 'Congradulations, you have guessed ', test.times, ' times'

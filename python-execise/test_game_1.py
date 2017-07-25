# test_game_1.py
# coding: utf-8
'''
锤子剪刀布游戏

思路：
定义两个类：
1. Game类 - 包含GAMELIST，锤子剪刀布，并用数组的下标来表示， 包含check_win()方法，返回赢，输，和平局
2. GameLaunch类 - 一直提示用户输入选择，三盘两胜制，直到用户win_time = 2盘，或者lose_time = 2盘，绕过了平局
3. 在main函数里，创建GameLaunch().launch()
'''
import random

class Game:
	def __init__(self,user_guess):
		self.GAMELIST = ['Chuizi','Bu','Jiandao']
		self.user_guess = user_guess-1
		self.computer_guess = int(random.random()*3)

	def check_win(self):
		user = self.GAMELIST[self.user_guess]
		computer = self.GAMELIST[self.computer_guess]
		if user == 'Chuizi':
			if computer == 'Chuizi':

				return 'Ping'
			elif computer == 'Jiandao':
				return 'Win'
			else:
				return 'Lose'
		elif user == 'Bu':
			if computer == 'Bu':
				return 'Ping'
			elif computer == 'Chuizi':
				return 'Win'
			else:
				return 'Lose'
		else:
			if computer == 'Jiandao':
				return 'Ping'
			elif computer == 'Bu':
				return 'Win'
			else:
				return 'Lose'

class LaunchGame:
	def __init__(self):
		self.win_time = 0
		self.lose_time = 0
		self.total_time = 0
	def launch(self):
		while True:
	
			print 'Please input your choice, 1: Chuizi, 2:Bu, 3:jiandao'
			user_guess = raw_input()
			self.total_time += 1
			game = Game(int(user_guess))
			result = game.check_win()
			print 'you', result
			if result == 'Win':
				self.win_time += 1
			if result == 'Lose':
				self.lose_time += 1
			
			if self.win_time == 2 or self.lose_time == 2:
				print 'you win time in ', self.total_time, 'is', self.win_time, 'lose time is ', self.lose_time
				if self.win_time > self.lose_time:
					print 'CONGRADULATIONS! YOU WIN'
				else:
					print 'PITY! YOU LOSE'
				break





if __name__ == '__main__':
	LaunchGame().launch()
	
	
	
	


	



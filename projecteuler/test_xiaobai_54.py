# test_xiaobai_54.py
# coding: utf-8
'''
   0 High Card: Highest value card.
   1 One Pair: Two cards of the same value.
   2 Two Pairs: Two different pairs.
   3 Three of a Kind: Three cards of the same value.
   4 Straight: All cards are consecutive values.
   5 Flush: All cards of the same suit.
   6 Full House: Three of a kind and a pair.
   7 Four of a Kind: Four cards of the same value.
   8 Straight Flush: All cards are consecutive values of same suit.
   9 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    玩poker




'''

class Poker:
	def __init__(self,p1,p2):
		self.Player1 = p1
		self.Player2 = p2
		self.suit_list1 = []
		self.suit_list2 = []
		self.number_list1 = []
		self.number_list2 = []
		self.sorted_number_list1 = []
		self.sorted_number_list2 = []
		self.level1 = -1
		self.level2 = -1

	def getNumber(self):
		tmp_list = self.Player1.split(' ')
		print tmp_list
		for item in tmp_list:
			self.suit_list1.append(item[-1])
			self.number_list1.append(item[:-1])
		
		tmp_list = self.Player2.split(' ')
		for item in tmp_list:
			self.suit_list2.append(item[-1])
			self.number_list2.append(item[:-1])


	def isSameSuit(self,suit_list):
		for item in suit_list:
			if item != suit_list[0]:
				return False
		return True
	def changeSort(self,number_list):
		tmp_list = []
		tmp_tmp_list =[]
		for item in number_list:
			if item == 'J':
				tmp_list.append('11')
			elif item == 'T':
				tmp_list.append('10')
			elif item == 'Q':
				tmp_list.append('12')
			elif item == 'K':
				tmp_list.append('13')
			elif item == 'A':
				tmp_list.append('14')
			else:
				tmp_list.append(item)
		tmp_tmp_list = sorted(tmp_list)
		return tmp_tmp_list
	def processNumberList(self):
		self.sorted_number_list1 = self.changeSort(self.number_list1)
		self.sorted_number_list2 = self.changeSort(self.number_list2)
	def isRoyalFlush(self,number_list, suit_list):
		
		if number_list == ['10','11','12','13','14'] and self.isSameSuit(suit_list):
			return 9
		else:
			return -1
	def isStraightFlush(self,number_list,suit_list):
		new_list = []
		for item in number_list:
			new_list.append(int(item))
		if new_list == [new_list[0],new_list[0]+1,new_list[0]+2, new_list[0]+3, new_list[0]+4] and self.isSameSuit(suit_list):
			return 8
		else:
			return -1
	def isFourKind(self,number_list,suit_list):
		new_list = []
		for item in number_list:
			new_list.append(int(item))
		if new_list[:-1] == [new_list[0],new_list[0],new_list[0],new_list[0]] or new_list[1:] == [new_list[1],new_list[1],new_list[1],new_list[1]]:
			return 7
		else:
			return -1
	def isFullHouse(self,number_list, suit_list):

		new_list = []
		for item in number_list:
			new_list.append(int(item))
		if new_list[0]==new_list[1] and new_list[2]==new_list[4] or new_list[0]==new_list[2] and new_list[3]==new_list[4]:
			return 6
		else:
			return -1
	def isFlush(self,number_list,suit_list):
		if self.isSameSuit(suit_list):
			return 5
		else:
			return -1
	def isStraight(self,number_list,suit_list):
		new_list = []
		for item in number_list:
			new_list.append(int(item))
		if new_list == [new_list[0],new_list[0]+1,new_list[0]+2, new_list[0]+3, new_list[0]+4]:
			return 4
		else:
			return -1
	def isThreeKind(self,number_list,suit_list):
		if number_list[0]==number_list[2] or number_list[1]==number_list[3] or number_list[2]==number_list[4]:
			return 3
		else:
			return -1
	def isTwoPairs(self,number_list,suit_list):
		if number_list[0]==number_list[1] and number_list[3]==number_list[4] or number_list[1]==number_list[2] and number_list[3]==number_list[4] or number_list[0]==number_list[1] and number_list[2]==number_list[3]:
			return 2
		else:
			return -1
	def isOnePairs(self,number_list, suit_list):
		if number_list[0]==number_list[1] or number_list[1]==number_list[2] or number_list[2]==number_list[3] or number_list[3]==number_list[4]:
			return 1
		else:
			return -1
	def checkWin(self):
		def isHighest():
			if int(self.sorted_number_list1[-1]) > int(self.sorted_number_list2[-1]):
				return True
			else:
				return False
		if self.level1 == self.level2 == 8:
			print 'They are both StrightFlush'
			if isHighest():
				return 'Player1 Win'
			else:
				return 'Player2 Win'
		if self.level1 == self.level2 == 5 :
			print 'They are both Flash'
			if isHighest():
				return 'Player1 Win'
			else:
				return 'Player2 Win'
		if self.level1 == self.level2 == 4 :
			print 'They are both Straight'
			if isHighest():
				return 'Player1 Win'
			else:
				return 'Player2 Win'

		if self.level1 == self.level2 == 7:
			print 'They are both Four Kind'
			for i in range(len(self.sorted_number_list1)-3):
				if self.sorted_number_list1[i] == self.sorted_number_list1[i+1]==self.sorted_number_list1[i+2]==self.sorted_number_list1[i+3]:
					value1 = self.sorted_number_list1[i]
					break
			for i in range(len(self.sorted_number_list2)-3):
				if self.sorted_number_list2[i] == self.sorted_number_list2[i+1]==self.sorted_number_list2[i+2]==self.sorted_number_list2[i+3]:
					value2 = self.sorted_number_list2[i]
					break
			if value1 > value2:
				return 'Player1 Win'
			else:
				return 'Player2 Win'
		if self.level1 == self.level2 == 3:
			print 'They are both Three Kind'
			for i in range(len(self.sorted_number_list1)-2):
				if self.sorted_number_list1[i] == self.sorted_number_list1[i+1]==self.sorted_number_list1[i+2]:
					value1 = self.sorted_number_list1[i]
					break
			for i in range(len(self.sorted_number_list2)-2):
				if self.sorted_number_list2[i] == self.sorted_number_list2[i+1]==self.sorted_number_list2[i+2]:
					value2 = self.sorted_number_list2[i]
					break
			if value1 > value2:
				return 'Player1 Win'
			else:
				return 'Player2 Win'
		if self.level1 == self.level2 == 0:
			print 'They are both High Card'
			if isHighest():
				return 'Player1 Win'

			else:
				return 'Player2 Win'

		elif self.level1 == self.level2 == 2:
			print 'They are two one pair'

			for i in range(len(self.sorted_number_list1)-1,0,-1):
				if self.sorted_number_list1[i] == self.sorted_number_list1[i-1]:
					value1 = self.sorted_number_list1[i]
					break
			for i in range(len(self.sorted_number_list2)-1,0,-1):
				if self.sorted_number_list2[i] == self.sorted_number_list2[i-1]:
					value2 = self.sorted_number_list2[i]
					break
			if value1 > value2:
				return 'Player1 Win'
			elif value1 < value2:
				return 'Player2 Win'
			else:
				if isHighest():
					return 'Player1 and Player2 has same one pair, but Player1 Win'
				else:
					return 'Player1 and Player2 has same one pair, but Player2 Win '		


		elif self.level1 == self.level2 == 1:
			print 'They are both one pair'

			for i in range(len(self.sorted_number_list1)-1):
				if self.sorted_number_list1[i] == self.sorted_number_list1[i+1]:
					value1 = self.sorted_number_list1[i]
					break
			for i in range(len(self.sorted_number_list2)-1):
				if self.sorted_number_list2[i] == self.sorted_number_list2[i+1]:
					value2 = self.sorted_number_list2[i]
					break
			if value1 > value2:
				return 'Player1 Win'
			elif value1 < value2:
				return 'Player2 Win'
			else:
				if isHighest():
					return 'Player1 and Player2 has same one pair, but Player1 Win'
				else:
					return 'Player1 and Player2 has same one pair, but Player2 Win '
		elif self.level1 == self.level2 == 6:
			print 'they are both 3 FullHouse'
			for i in range(len(self.sorted_number_list1)-2):
				if self.sorted_number_list1[i] == self.sorted_number_list1[i+1]==self.sorted_number_list1[i+2]:
					value1 = self.sorted_number_list1[i]
					break
			for i in range(len(self.sorted_number_list2)-2):
				if self.sorted_number_list2[i] == self.sorted_number_list2[i+1]==self.sorted_number_list2[i+2]:
					value2 = self.sorted_number_list2[i]
					break
			if value1 > value2:
				return 'Player1 Win'
			elif value1 < value2:
				return 'Player2 Win'
			else:
				if isHighest():
					return 'Player1 and Player2 has same one pair, but Player1 Win'
				else:
					return 'Player1 and Player2 has same one pair, but Player2 Win'

		elif self.level1 > self.level2:
			return 'Player1 Win'
		else:
			return 'Player2 Win'

	def get2Level(self):
		level1_list = []
		level1_list.append(self.isRoyalFlush(self.sorted_number_list1,self.suit_list1))
		
		level1_list.append(self.isStraightFlush(self.sorted_number_list1,self.suit_list1))
	
		level1_list.append(self.isFourKind(self.sorted_number_list1,self.suit_list1))
		
		level1_list.append(self.isFullHouse(self.sorted_number_list1,self.suit_list1))
		
		level1_list.append(self.isFlush(self.sorted_number_list1,self.suit_list1))
		
		level1_list.append(self.isStraight(self.sorted_number_list1,self.suit_list1))
		
		level1_list.append(self.isThreeKind(self.sorted_number_list1,self.suit_list1))
		
		level1_list.append(self.isTwoPairs(self.sorted_number_list1,self.suit_list1))
		level1_list.append(self.isOnePairs(self.sorted_number_list1, self.suit_list1))
		level1_list.append(0)
		self.level1 = max(level1_list)

		level2_list = []
		level2_list.append(self.isRoyalFlush(self.sorted_number_list2,self.suit_list2))
		
		level2_list.append(self.isStraightFlush(self.sorted_number_list2,self.suit_list2))
	
		level2_list.append(self.isFourKind(self.sorted_number_list2,self.suit_list2))
		
		level2_list.append(self.isFullHouse(self.sorted_number_list2,self.suit_list2))
		
		level2_list.append(self.isFlush(self.sorted_number_list2,self.suit_list2))
		
		level2_list.append(self.isStraight(self.sorted_number_list2,self.suit_list2))
		
		level2_list.append(self.isThreeKind(self.sorted_number_list2,self.suit_list2))
		
		level2_list.append(self.isTwoPairs(self.sorted_number_list2,self.suit_list2))
		level2_list.append(self.isOnePairs(self.sorted_number_list2,self.suit_list2))
		print level2_list
		level2_list.append(0)
		self.level2 = max(level2_list)


if __name__ == '__main__':
	Player1 = '5H 5C 6S 7S KD'
	Player2 = '2C 3S 8S 8D 9D'
	Player3 = '10D JD KD QD AD'
	Player4 = '4C 5C 6C 7C 8C'
	Player5 = 'KC KD KH KS AS'
	Player6 = '1C 1D 1H 3S 3C'
	Player7 = '5D 8C 9S JS AC'
	Player8 = '2C 5C 7D 8S QC'
	Player9 = '2D 9C AS AH AC'
	Player10 = '3D 6D 7D 9D QD'
	Player11 = '4D 6S 9H QH QC'
	Player12 = '3D 6D 7H QD QS'
	Player13 = '2H 2D 4C 4D 4S'
	Player14 = '3C 3D 3S 9S 9D'
	myfile = open('p054_poker.txt')
	player1_list = []
	player2_list = []
	player2_count = 0
	player1_count = 0
	for line in myfile.readlines():
		
		player1_list.append(line[:14])
		player2_list.append(line[15:-1])
	print player1_list, player2_list
	for i in range(len(player1_list)):

		test = Poker(player1_list[i],player2_list[i])
		test.getNumber()
		test.processNumberList()
		print test.sorted_number_list1,test.suit_list1
		print test.sorted_number_list2, test.suit_list2
		test.get2Level()
		print test.level1
		print test.level2
		
		if 'Player2 Win' in test.checkWin():
			player2_count += 1
		else:
			player1_count += 1
	print player1_count, player2_count

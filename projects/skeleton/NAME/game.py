# game.py
# coding: utf-8
class Room(object):
	def __init__(self,name,description):
		self.name = name
		self.description = description
		self.paths = {} #字典

	def go(self,direction):
		return self.paths.get(direction,None)

	def add_paths(self,paths):
		self.paths.update(paths)


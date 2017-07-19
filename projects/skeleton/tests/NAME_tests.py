# NAME_tests.py
# coding: utf-8
from nose.tools import *
from NAME.game import Room

# def setup():
# 	print 'SETUP'

# def teardown():
# 	print 'TEARDOWN'

# def test_basic():
# 	print 'I RAN'

def test_room():
	gold = Room('GoldRoom','''This room has gold
		you can grab. There is a door to the north.
		''')
	assert_equal(gold.name, 'GoldRoom')
	assert_equal(gold.paths, {})

def test_room_paths():
	center = Room('CenterRoom','Test room in the centor')
	north = Room('NorthRoom','Test room in the north')
	south = Room('SouthRoom','Test room in the south')

	center.add_paths({'north':north, 'south':south})
	assert_equal(center.go('north'),north)
	assert_equal(center.go('south'),south)

def test_map():
	start = Room('Start','you can go west and down a hole')
	west = Room('Trees','There are trees here, you can go east')
	down = Room('Dungeon','It is dark down here, you can go up')

	start.add_paths({'west':west, 'down':down})
	west.add_paths({'east':start})
	down.add_paths({'up':start})

	assert_equal(start.go('west'),west)
	assert_equal(start.go('west').go('east'),start)
	assert_equal(start.go('down').go('up'),start)
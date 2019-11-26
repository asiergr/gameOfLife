"""
Script for testing gameOfLife.py
"""
from gameOfLife import *

"""
Sample boards
"""
board1 = 	[
			[0, 0, 0],
			[0, 0, 0],
			[0, 0, 0]
			]
board2 = 	[
			[1, 0, 0],
			[0, 0, 0],
			[0, 0, 1]
			]
board3 = 	[
			[0, 0, 0],
			[0, 0, 1],
			[0, 0, 0]
			]

"""
Testing neighboor count
"""
board = Board(state = board2)
print(board)
board.__next_state__()
print(board)
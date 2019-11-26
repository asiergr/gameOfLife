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
			[1, 1, 0],
			[0, 0, 0]
			]
board3 = 	[
			[1, 1, 1],
			[1, 1, 1],
			[1, 1, 1]
			]

"""
Testing neighboor count
"""
board = Board(state = board3)
print(board)
board.__next_state__()
print(board)
board.__next_state__()
print(board)
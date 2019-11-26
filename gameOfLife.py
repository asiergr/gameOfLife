"""
Milestones:
- Build data structure to store board state
- "Pretty -print" board on terminal
- Given starting board game, calculate next state
- Run game forever
Extensions:
- Save cool starting positions to files and be able to reload them
- Imporove UI
. Change rules
"""

"""
Imports
"""
import random as rd

"""
Building the Board
"""
class Board:
	def __init__(self, width, height, random = True): # Default init to random board
		self.width = width
		self.height = height
		self.random = random

		# Build the random board
		self.state = []
		for j in range(self.height):
			self.state.append([])
			for i in range(self.width):
				self.state[j].append(rd.randint(0,1))

"""
Testing
"""
b = Board(3,3)
print(b.state)


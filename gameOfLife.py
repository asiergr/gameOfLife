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

	def __str__(self):
		hor_edges = ''
		for i in range(2*self.width - 1):
			hor_edges += '-'
		pretty_rows = hor_edges + '\n'
		for row in self.state:
			for n in range(len(row)):
				if n == 0:
					if row[n] == 0:
						pretty_rows += '|0'
					if row[n] == 1:
						pretty_rows += '|1'
				elif n == self.width - 1:
					if row[n] == 0:
						pretty_rows += '0|\n'
					if row[n] == 1:
						pretty_rows += '1|\n'

				elif row[n] == 0:
					pretty_rows += '0'
				elif row[n] == 1:
					pretty_rows += '1'
		pretty_rows += hor_edges

		return pretty_rows

	def __repr__(self):
		return f"Board with {self.height} rows and {self.width} columns"

	


"""
Testing
"""
b = Board(3,3)
print(b)


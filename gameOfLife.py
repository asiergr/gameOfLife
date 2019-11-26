"""
Milestones:
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
Helper functions
"""
def neighboor_counter(board_object, x_coord, y_coord):
	neighboor_count = 0
	try:
		for i in range(3):
			for j in range(3):
				#Use the fact that 1s and 0s are used to represent live/dead
				neighboor_count += board_object.state[x_coord + i][y_coord + j]
	except IndexError:
		pass
	return neighboor_count

"""
Classes
"""
class Board:
	def __init__(self, width, height, state = []): # Default init to random board
		self.width = width
		self.height = height
		self.state = state

		# Build the random board if no arg passed in
		if self.state == []:
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

	# Function to count neighboors


	def __next_state__(self):
		# Create a new temp board
		temp_board = []
		for j in range(self.height):
			temp_board.append([])
			for i in range(self.width):
				temp_board[j].append(0)

		# Now we calculate for the existing board
		for y in range(self.height):
			for x in range(self.width):
				neighboor_n = neighboor_counter(self, x, y)
				if neighboor_n < 2 and self.state[x][y] == 1:
					temp_board[x][y] = 0
				elif neighboor_n == 2 or neighboor_n == 3 and self.state[x][y] == 1:
					temp_board[x][y] = 1
				elif neighboor_n > 3 and self.state[x][y] == 1:
					temp_board[x][y] = 0
				elif neighboor_n == 3 and self.state[x][y] == 0:
					temp_board[x][y] = 1
		# Update the board
		self.state = temp_board





"""
Testing
"""
b = Board(3,3)
print(b)
b.__next_state__()
print(b)


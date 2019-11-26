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
import time

"""
Helper functions
"""
def neighboor_counter(board_object, y_coord, x_coord):
	neighboor_count = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			# Only positive indexing and avoid the place of the cell itself
			if y_coord + i >= 0 and x_coord + j >= 0 and (y_coord + i, x_coord + j) != (y_coord, x_coord):
				try:
				# Use the fact that 1s and 0s are used to represent live/dead
					neighboor_count += board_object.state[y_coord + i][x_coord + j]
				except IndexError:
					continue
					

	return neighboor_count

"""
Classes
"""
class Board:
	def __init__(self, width = 0, height = 0, state = []): # Default init to random board
		self.state = state

		if self.state == []:
			self.width = width
			self.height = height
		else:
			self.height = len(self.state)
			self.width = len(self.state[0])

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
				neighboor_n = neighboor_counter(self, y, x)

				if neighboor_n < 2 and self.state[y][x] == 1:
					temp_board[y][x] = 0
				elif (neighboor_n == 2 or neighboor_n == 3) and self.state[y][x] == 1:
					temp_board[y][x] = 1
				elif neighboor_n > 3 and self.state[y][x] == 1:
					temp_board[y][x] = 0
				elif neighboor_n == 3 and self.state[y][x] == 0:
					temp_board[y][x] = 1
		# Update the board
		self.state = temp_board

	def __run__(self):
		live_count = 1

		while live_count != 0:
			live_count = 0
			for row in self.state:
				for cell in row:
					live_count += cell

			self.__next_state__()
			print(self)
			time.sleep(1)
		print("Everyone is dead.")





"""
Running
"""

board = Board(6, 6)
board.__run__()

"""
To do:
- Add catch for passing in an invalid board
"""


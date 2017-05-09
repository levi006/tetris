"""Tetris  clone."""

import sys
import curses


class Tetrimino(object):
	"""Generic piece."""

	def __init__(self, rot=0, y=0, x=0, window=None):
		"""Create piece with initial rotation."""

		self.rot = rot
		self.y = y
		self.x = x
		self.window = window 

	def rot_cw(self):
		"""Rotate CW."""

		self.rot = (self.rot + 1) % 4

	def rot_ccw(self):
		"""Rotate CCW."""

		self.rot = (self.rot - 1) % 4

	def draw_piece(self):
		"""Draws a tetrimino."""
		for y, row in enumerate(self.rots[self.rot]):
			for x, cell in enumerate(row):
				if cell == "1":
					self.window.addch(self.y + y +1, self.x + x + 1, 65)

	def move(self, dx=0, dy=0):
		"""Move piece by delta-x and delta-y.

		Checks to make sure move is legal.
		"""

		curr = self.rots[self.rot]

		# within the NxM grid of this piece, what's the min/max x/y coords
		# (ie, "bounding box of pixels actually used")
		
		# TODO: this isn't right!
		
		min_x = min(b[y][0] for y in range(height) if 
		max_x = max(r[-1] for r in curr)
		min_y = min(b[0][x] for x in range(width))
		max_y = max(b[-1][x] for x in range(width))

		if 




	def __str__(self):
		"""Show piece."""

		out = ""

		for row in self.rots[self.rot]:
			out += " ".join(row) + "\n"

		# Trim newline on last line, since __str__ doesn't expect it
		return out[:-1]

class PI(Tetrimino):
	"""Long piece.

		>>> pi = PI()
		>>> pi.rot
		0
		>>> print pi
		1 1 1 1
		. . . .
		. . . .
		. . . .

		>>> pi.rot_cw()
		>>> pi.rot
		1
		>>> print pi
		. 1 . .
		. 1 . .
		. 1 . .
		. 1 . .

		>>> pi.rot_cw()
		>>> pi.rot
		2
		>>> print pi
		1 1 1 1
		. . . .
		. . . .
		. . . .

		>>> pi.rot_cw()
		>>> pi.rot
		3
		>>> print pi
		. 1 . .
		. 1 . .
		. 1 . .
		. 1 . .

		>>> pi.rot_cw()
		>>> pi.rot
		0

		>>> pi.rot_ccw()
		>>> pi.rot
		3
	"""

	r1 = ["1111",
		  "....",
		  "....",
		  "...."]

	r2 = [".1..",
		  ".1..",
		  ".1..",
		  ".1.."]

	rots = [r1,r2,r1,r2]

class PJ(Tetrimino):
	""" """

	r1 = [".1.",
		  ".1.",
		  "11."]	
	
	r2 = ["...",
	      "1..",
	      "111"]

	r3 = ["11.",
		  "1..",
		  "1.."]

	r4 = ["111",
          "..1",
          "..."]

	rots = [r1,r2,r3,r4]

class PL(Tetrimino):
	""" """

	r1 = [".1.",
		  ".1.",
		  ".11"]
	
	r2 = ["...",
	 	  "111",
	 	  "1.."]
	

	r3 = [".11",
		  "..1",
		  "..1"]
	
	r4 = ["...",
	 	  "..1",
	 	  "111"]

	rots = [r1,r2,r3,r4]

class PO(Tetrimino):
	""" """

	r1 = ["11",
		  "11"]

	rots = [r1,r1,r1,r1]

class PS(Tetrimino):
	""" """

	r1 = [".1.",
		  ".11",
		  "..1"]
	
	r2 = ["...",
	 	  ".11",
	 	  "11."]
	

	rots = [r1,r2,r1,r2]

class PT(Tetrimino):
	""" """


	r1 = ["111",
		  ".1.",
		  "..."]
	
	r2 = ["..1",
	 	  "111",
	 	  "..1"]
	

	r3 = ["...",
		  ".1.",
		  "111"]
	
	r4 = ["1..",
	 	  "11.",
	 	  "1.."]

	rots = [r1,r2,r3,r4]


class PZ(Tetrimino):
	""" """
	r1 = [".1.",
		  "11.",
		  "1.."]
	
	r2 = ["...",
	 	  "11.",
	 	  ".11"]
	

	rots = [r1,r2,r1,r2]


class Board(object):
	"""Playing board.

	The board is a y-by-x grid.

		>>> b = Board()

	Make sure it's the right size:

		>>> b.grid[29][11]
		0

		>>> b.grid[30][11]
		Traceback (most recent call last):
			...
		IndexError: list index out of range

	Make sure that changing one cell doesn't change others:

		>>> b.grid[0][0] = 1
		>>> b.grid[1][0]
		0
		>>> b.grid[0][1]
		0

	"""

	def __init__(self, width=12, height=30):
		self.width = width
		self.height = height

		self.grid = [[0] * width for y in range(height)]
		
	def curses_board(self):
		self.window = curses.newwin(self.height + 2, self.width + 2, 1, 1)
		# self.window.addstr(10, 10, "Hello")
		piece = PL(window=self.window)
		for i in range(4):
			self.window.clear()
			self.window.box()
			piece.draw_piece()
			self.window.refresh()
			self.window.getch()
			piece.rot_cw()

def game(stdscr):
	board = Board()
	board.curses_board()
	stdscr.addstr(20, 20, "Yo")
	stdscr.box()
	stdscr.refresh()

	





if __name__ == "__main__":

	if len(sys.argv) > 1 and sys.argv[1] == "play":
		curses.wrapper(game)

	else:
		import doctest
		if doctest.testmod().failed == 0:
			print "\n*** GO GO GO\n"

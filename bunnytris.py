"""Tetris  clone."""

class Tetrimino(object):
	"""Generic piece."""


class PI(Tetrimino):
	""" """

class PJ(Tetrimino):
	""" """

class PL(Tetrimino):
	""" """

class PO(Tetrimino):
	""" """

class PS(Tetrimino):
	""" """

class PT(Tetrimino):
	""" """

class PZ(Tetrimino):
	""" """



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
		self.grid = [[0] * width for y in range(height)]



if __name__ == "__main__":
	import doctest
	if doctest.testmod().failed == 0:
		print "\n*** GO GO GO\n"

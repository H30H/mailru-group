import unittest
from main import TicTacToe


class MyTestTicTacToe(unittest.TestCase):
	def test_asserts(self):
		self.field = TicTacToe()
		self.assertRaises(ValueError, lambda: self.field.turn(3, 3))
		self.assertRaises(ValueError, lambda: self.field.turn(-1, -1))
		self.assertEqual(self.field.turn(0, 0), False)
		self.assertRaises(ValueError, lambda: self.field.turn(0, 0))

	def test_tiy_game(self):
		self.field = TicTacToe()
		self.assertEqual(self.field.turn(1, 1), False)  # |2|6|5|   |0|0|X|
		self.assertEqual(self.field.turn(0, 0), False)  # |8|1|4|   |X|X|0|
		self.assertEqual(self.field.turn(2, 2), False)  # |9|7|3|   |0|X|X|
		self.assertEqual(self.field.turn(2, 1), False)
		self.assertEqual(self.field.turn(2, 0), False)
		self.assertEqual(self.field.turn(1, 0), False)
		self.assertEqual(self.field.turn(1, 2), False)
		self.assertEqual(self.field.turn(0, 2), False)
		self.assertRaises(Warning, lambda: self.field.turn(0, 1))

	def test_player1_win(self):
		self.field = TicTacToe()
		self.assertEqual(self.field.turn(1, 1), False)  # |7| |4|   |X| |0|
		self.assertEqual(self.field.turn(1, 2), False)  # |5|1|6|   |X|X|0|
		self.assertEqual(self.field.turn(0, 2), False)  # |3|2| |   |X|0| |
		self.assertEqual(self.field.turn(2, 0), False)
		self.assertEqual(self.field.turn(0, 1), False)
		self.assertEqual(self.field.turn(2, 1), False)
		self.assertEqual(self.field.turn(0, 0), True)
		self.assertEqual(self.field.whose_turn, True)

	def test_player2_win(self):
		self.field = TicTacToe()
		self.assertEqual(self.field.turn(1, 1), False)  # | | |2|   | | |0|
		self.assertEqual(self.field.turn(2, 0), False)  # |5|1|4|   |X|X|0|
		self.assertEqual(self.field.turn(0, 2), False)  # |3| |6|   |X| |0|
		self.assertEqual(self.field.turn(2, 1), False)
		self.assertEqual(self.field.turn(0, 1), False)
		self.assertEqual(self.field.turn(2, 2), True)
		self.assertEqual(self.field.whose_turn, False)


if __name__ == '__main__':
	unittest.main()

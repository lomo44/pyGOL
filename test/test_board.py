import unittest
from board import Board
import numpy as np
class test_board(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    def test_initialize(self):
        self.assertIsInstance(self.board,np.array)


if __name__ == "__main__":
    unittest.main()

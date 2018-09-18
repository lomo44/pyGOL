import unittest
from board import Board
import numpy as np
class test_board(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.generate(5,5)
    def test_initialize(self):
        self.assertIsInstance(self.board.board,type(np.array([1,2,3])))
        
if __name__ == "__main__":
    unittest.main()

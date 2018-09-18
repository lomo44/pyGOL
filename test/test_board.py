import unittest
from board import Board
import numpy as np
class test_board(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.setBoard([[1,1,1],[1,1,1],[1,1,1]])
    def test_getElement(self):
        self.assertEqual(self.board.board[(0,0)],1)
    def test_initialize(self):
        self.assertIsInstance(self.board.board,type(np.array([1,2,3])))
    def test_getAliveNeighbor(self):
        self.assertEqual(self.board.getNumOfAliveNeighbor(1,1),8)

class test_senarios(unittest.TestCase):
    def test_UnderPopulation(self):
        a = Board()
        a.setBoard([[0,0,0],[0,1,0],[0,0,0]])
        self.assertEqual(0,a.getNextState(1,1))
    def test_Surive2(self):
        a = Board()
        a.setBoard([[1,1,0],[0,1,0],[0,0,0]])
        self.assertEqual(1,a.getNextState(1,1))
        pass
    def test_Surive3(self):
        a = Board()
        a.setBoard([[1,1,1],[0,1,0],[0,0,0]])
        self.assertEqual(1,a.getNextState(1,1))
        pass
    def test_OverCrowding(self):
        a = Board()
        a.setBoard([[1,1,1],[0,1,0],[1,0,0]])
        self.assertEqual(0,a.getNextState(1,1))
    def test_Reproduction(self):
        a = Board()
        a.setBoard([[1,1,1],[0,0,0],[0,0,0]])
        self.assertEqual(1,a.getNextState(1,1))
        pass
if __name__ == "__main__":
    unittest.main()

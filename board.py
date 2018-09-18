
from enum import Enum
import random
import numpy as np


class eCellState(Enum):
    UNDEFINED=0
    ALIVE=1
    DEAD=2


class Board:
    board = None   
    def generate(self,x,y):
        self.board = np.random.random_integers(0,3,(x,y))
    def setBoard(self,x): 
        self.board = np.array(x)
    def nextGen(self):
        pass
    def getNumOfAliveNeighbor(self,x,y):
        pass
    def getNumOfDeadNeighbor(self,x,y):
        pass
    def printBoard(self):
        print(self.board)

if __name__ == "__main__":
    a = Board()
    a.setBoard(np.array([[1,1,1],[1,0,1],[1,1,1]]))
    a.printBoard()
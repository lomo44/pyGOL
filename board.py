
from enum import Enum
import random
import numpy as np

class eCellState:
    ALIVE=1
    DEAD=0


class Board:
    board = None
    x = None
    y = None   
    def generate(self,x,y):
        self.board = np.random.random_integers(0,2,(x,y))
        self.x = x
        self.y = y
    def setBoard(self,x): 
        self.board = np.array(x)
        self.x = self.board.shape[0]
        self.y = self.board.shape[1]
    def nextGen(self):
        #TODO:
        pass
    def getNextState(self, x, y):
        AliveNei = self.getNumOfAliveNeighbor(x, y)
        if self.board[(x,y)] == eCellState.ALIVE:
            if AliveNei < 2:
                return eCellState.DEAD
            elif AliveNei == 2 or AliveNei == 3:
                return eCellState.ALIVE
            elif AliveNei > 3:
                return eCellState.DEAD
        else:
            if AliveNei == 3:
                return eCellState.ALIVE
            else:
                return eCellState.DEAD

    def getNumOfAliveNeighbor(self,x,y):
        # Wrapped board, need test
        tl = ((x + self.x - 1)%self.x,(y + self.y - 1)%self.y)
        ml = ((x + self.x - 1)%self.x,y)
        bl = ((x + self.x - 1)%self.x,(y + self.y + 1)%self.y)
        tm = (x,(y + self.y - 1)%self.y)
        bm = (x,(y + self.y + 1)%self.y)
        tr = ((x + self.x + 1)%self.x,(y + self.y - 1)%self.y)
        mr = ((x + self.x + 1)%self.x,y)
        br = ((x + self.x + 1)%self.x,(y + self.y + 1)%self.y)
        alive_count = 0
        alive_count += 1 if self.board[tl] == eCellState.ALIVE else 0
        alive_count += 1 if self.board[ml] == eCellState.ALIVE else 0
        alive_count += 1 if self.board[bl] == eCellState.ALIVE else 0
        alive_count += 1 if self.board[tm] == eCellState.ALIVE else 0
        alive_count += 1 if self.board[bm] == eCellState.ALIVE else 0
        alive_count += 1 if self.board[tr] == eCellState.ALIVE else 0
        alive_count += 1 if self.board[mr] == eCellState.ALIVE else 0
        alive_count += 1 if self.board[br] == eCellState.ALIVE else 0
        return alive_count

    def printBoard(self):
        print(self.board)

if __name__ == "__main__":
    a = Board()
    a.setBoard(np.array([[1,1,1],[1,0,1],[1,1,1]]))
    a.printBoard()
import os

class Life:
    def __init__(self, nLin, nCol) -> None:
        self.nLin = nLin
        self.nCol = nCol
        self.board = [[0]*nLin for i in range(nCol)]
    def print_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.nLin):
            print("\n")
            for j in range(self.nCol):
                print(self.board[i][j], end="")
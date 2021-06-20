# Design Tic-Tac-Toe
# https://leetcode.com/problems/design-tic-tac-toe/
class TicTacToe(object):

    def __init__(self, n):
        self.rows = [[0 for col in range(n)] for row in range(n)]
        self.cols = [[0 for col in range(n)] for row in range(n)]
        self.diagonal = [0 for i in range(n)]
        self.antiDiagonal = [0 for i in range(n)]
        self.n = n
        """
        Initialize your data structure here.
        :type n: int
        """
    
    def ifInDiagonal(self, row, col):
        if(row == col):
            return True
        return False
    
    def ifInAntiDiagonal(self, row, col):
        if(col == (self.n-row-1)):
            return True
        return False
    
    def addToDiagonal(self, row, col, player):
        if(self.ifInDiagonal(row, col)):
            self.diagonal[row] = player
        if(self.ifInAntiDiagonal(row, col)):
            self.antiDiagonal[row] = player
    
    def addToRow(self, row, col, player):
        self.rows[row][col] = player
    
    def addToCol(self, row, col, player):
        self.cols[col][row] = player
    
    def isWin(self, row, col, player):
        if(player == 1):
            otherPlayer = 2
        else:
            otherPlayer = 1
        # row
        if((player in self.rows[row]) and (otherPlayer not in self.rows[row]) and (0 not in self.rows[row])):
            return True
        # col
        if((player in self.cols[col]) and (otherPlayer not in self.cols[col]) and (0 not in self.cols[col])):
            return True
        # diagonal
        if(self.ifInDiagonal(row, col)):
            if((player in self.diagonal) and (otherPlayer not in self.diagonal) and (0 not in self.diagonal)):
                return True
        # antiDiagonal
        if(self.ifInAntiDiagonal(row, col)):
            if((player in self.antiDiagonal) and (otherPlayer not in self.antiDiagonal) and (0 not in self.antiDiagonal)):
                return True
            
    def move(self, row, col, player):
        self.addToRow(row, col, player)
        self.addToCol(row, col, player)
        self.addToDiagonal(row, col, player)
        if(self.isWin(row, col, player)):
            return player
        return 0
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)

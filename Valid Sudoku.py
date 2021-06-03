# https://leetcode.com/problems/valid-sudoku/
# Valid Sudoku
class Solution(object):
    def getRange(self,bound):
        if(bound >= 0 and bound < 3):
            return [0,3]
        if(bound >= 3 and bound < 6):
            return [3,6]
        if(bound >= 6 and bound < 9):
            return [6,9]
    
    def isPresentInGrid(self, board, row, col):
        rBound = self.getRange(row)
        cBound = self.getRange(col)
        for r in range(rBound[0], rBound[1]):
            for c in range(cBound[0], cBound[1]):
                if(r != row and c != col):
                    if(board[r][c] == board[row][col]):
                        return True
        return False
        
    def isPresentInRow(self, board, row, col):
        for index in range(len(board)):
            if(index != col):
                if(board[row][index] == board[row][col]):
                    return True
        return False
    
    def isPresentInCol(self, board, row, col):
        for index in range(len(board[row])):
            if(index != row):
                if(board[index][col] == board[row][col]):
                    return True
        return False
        
    def isValidSudoku(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if(board[row][col] != "."):
                    if (self.isPresentInRow(board, row, col)):
                        return False
                    if (self.isPresentInCol(board, row, col)):
                        return False
                    if (self.isPresentInGrid(board, row, col)):
                        return False
        return True
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        

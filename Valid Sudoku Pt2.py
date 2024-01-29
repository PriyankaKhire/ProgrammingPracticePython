# Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/description

class Solution(object):
    def validateRow(self, board, row):
        # Collect all numbers of the row in a hash map
        num = {}
        for col in range(len(board[0])):
            if (board[row][col] == "."):
                continue
            if (board[row][col] in num):
                return False
            num[board[row][col]] = True
        return True

    def validateCol(self, board, col):
        # Collect all numbers of the col in a hash map
        num = {}
        for row in range(len(board)):
            if (board[row][col] == "."):
                continue
            if (board[row][col] in num):
                return False
            num[board[row][col]] = True
        return True
    
    def getSubBoxCell(self, cell):
        if (cell >= 0 and cell <= 2):
            return [0, 1, 2]
        if (cell >= 3 and cell <= 5):
            return [3, 4, 5]
        if (cell >=6 and cell <= 8):
            return [6, 7, 8]
    
    def getSubBox(self, row, col):
        # get cells for row
        rowCellNumbers = self.getSubBoxCell(row)
        # get cells for col
        colCellNumbers = self.getSubBoxCell(col)
        cells = []
        for r in rowCellNumbers:
            for c in colCellNumbers:
                cells.append([r,c])
        return cells
    
    
    def validate3X3(self, board, row, col):
        cells = self.getSubBox(row, col)
        num = {}
        for cell in cells:
            if (board[cell[0]][cell[1]] == "."):
                continue
            if (board[cell[0]][cell[1]] in num):
                return False
            num[board[cell[0]][cell[1]]] = True
        return True

    def isValidSudoku(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                # Validate row
                if not(self.validateRow(board, row)):
                    return False
                # Validate col
                if not(self.validateCol(board, col)):
                    return False
                # Validate 3x3 box
                if not(self.validate3X3(board, row, col)):
                    return False
        return True
        """
        :type board: List[List[str]]
        :rtype: bool
        """

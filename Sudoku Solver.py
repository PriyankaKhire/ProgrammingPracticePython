# Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/submissions/

class Solution(object):
    def __init__(self):
        self.rows = {i:[] for i in range(10)}
        self.cols = {i:[] for i in range(10)}
        self.grids = {i:[] for i in range(10)}
    
    def getBounds(self, boundry):
        if(boundry >=0 and boundry < 3):
            return [0, 3]
        if(boundry >=3 and boundry < 6):
            return [3, 6]
        if(boundry >=6 and boundry < 9):
            return [6, 9]
    
    def getGridNumber(self, row, col):
        rBoundry = self.getBounds(row)
        cBoundry = self.getBounds(col)
        if(rBoundry == [0,3]):
            if(cBoundry == [0,3]):
                return 0
            if(cBoundry == [3,6]):
                return 1
            if(cBoundry == [6,9]):
                return 2
        if(rBoundry == [3,6]):
            if(cBoundry == [0,3]):
                return 3
            if(cBoundry == [3,6]):
                return 4
            if(cBoundry == [6,9]):
                return 5
        if(rBoundry == [6,9]):
            if(cBoundry == [0,3]):
                return 6
            if(cBoundry == [3,6]):
                return 7
            if(cBoundry == [6,9]):
                return 8
    
    def putInGrid(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                if(board[row][col] != "."):
                    gridNum = self.getGridNumber(row, col)
                    self.grids[gridNum].append(board[row][col])
    
    def putInRows(self, board):
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (board[r][c] != "."):
                    self.rows[r].append(board[r][c])
    
    def putInCols(self, board):
        for c in range(len(board[0])):
            for r in range(len(board)):
                if(board[r][c] != "."):
                    self.cols[c].append(board[r][c])
    
    def initialSetup(self, board):
        self.putInRows(board)
        self.putInCols(board)
        self.putInGrid(board)
    
    def addElement(self, board, row, col, element):
        # add to board
        board[row][col] = element
        # add to row
        self.rows[row].append(element)
        # add to column
        self.cols[col].append(element)
        # add to grid
        gridNum = self.getGridNumber(row, col)
        self.grids[gridNum].append(element)
    
    def removeElement(self, board, row, col, element):
        # remove from board
        board[row][col] = "."
        # remove from row
        self.rows[row].remove(element)
        # remove from col
        self.cols[col].remove(element)
        # remove from grid
        gridNum = self.getGridNumber(row, col)
        self.grids[gridNum].remove(element)
    
    def isSafeToAddElement(self,row, col, element):
        # check if element present in row
        if (element in self.rows[row]):
            return False
        # check if element present in col
        if (element in self.cols[col]):
            return False
        # check if element present in grid
        gridNum = self.getGridNumber(row, col)
        if (element in self.grids[gridNum]):
            return False
        return True
    
    def findNextEmptySpace(self, board, row, col):
        for r in range(row, len(board)):
            for c in range(len(board[0])):
                if(board[r][c] == "."):
                    return [r, c]
        # No empty space is found
        return [-1,-1]
                
    
    def logic(self, board, row, col):
        #print row, col, board[row]
        nextFree = self.findNextEmptySpace(board, row, col)
        if(nextFree == [-1, -1]):
            #print "no more free", row, col, board
            return True
        for element in range(1, 10):
            strElement = str(element)
            if(self.isSafeToAddElement(nextFree[0], nextFree[1], strElement)):
                self.addElement(board, nextFree[0], nextFree[1], strElement)
                if(self.logic(board, nextFree[0], nextFree[1])):
                    return True
                #print "Element backtracking",strElement,"row", nextFree[0],"and column",nextFree[1]
                self.removeElement(board, nextFree[0], nextFree[1], strElement)
        #print "Backtracking for row", nextFree[0],"and column",nextFree[1]
        
        
        
        
    
    def solveSudoku(self, board):
        self.initialSetup(board)
        self.logic(board, 0, 0)
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        

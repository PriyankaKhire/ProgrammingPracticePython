# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

class Boundries(object):
    def __init__(self):
        self.rowStart = None
        self.rowEnd = None
        self.colStart = None
        self.colEnd = None
        
class Solution(object):
    
    # shrink boundries of the matrix for spiral print.
    def setBoundries(self, matrix, decreaseBy):
        boundries = Boundries()
        # set row boundry
        boundries.rowStart = 0 + decreaseBy
        boundries.rowEnd = len(matrix) - decreaseBy
        # set column boundry
        boundries.colStart = 0 + decreaseBy
        boundries.colEnd = len(matrix[0]) - decreaseBy
        return boundries
    
    def markCellVisitedAddToSpiralPrint(self, matrix, row, col, spiralPrint):
        # if the cell has not been visited
        if (matrix[row][col] != "visited"):
            spiralPrint.append(matrix[row][col])
        # mark the cell visited
        matrix[row][col] = "visited"
        
    def printSpiral(self, matrix, boundries, spiralPrint):
        # print first row
        for col in range(boundries.colStart, boundries.colEnd):
            self.markCellVisitedAddToSpiralPrint(matrix, boundries.rowStart, col, spiralPrint)
        # print last col
        for row in range(boundries.rowStart+1, boundries.rowEnd-1):
            self.markCellVisitedAddToSpiralPrint(matrix, row, boundries.colEnd-1, spiralPrint)
        # print last row in reverse
        for col in range(boundries.colEnd-1, boundries.colStart-1, -1):
            self.markCellVisitedAddToSpiralPrint(matrix, boundries.rowEnd-1, col, spiralPrint)
        # print first col
        for row in range(boundries.rowEnd-2, boundries.rowStart, -1):
            self.markCellVisitedAddToSpiralPrint(matrix, row, boundries.colStart, spiralPrint)
        
    def spiralOrder(self, matrix):
        spiralPrint = []
        boundryIndex = 0
        boundries = self.setBoundries(matrix, boundryIndex)
        # shirnk boundries until bounds are equal.
        while(boundries.rowStart < boundries.rowEnd and boundries.colStart < boundries.colEnd):
            boundryIndex = boundryIndex + 1
            self.printSpiral(matrix, boundries, spiralPrint)
            boundries = self.setBoundries(matrix, boundryIndex)
        return spiralPrint
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        

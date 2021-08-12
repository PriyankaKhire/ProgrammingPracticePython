# Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution(object):
    def __init__(self):
        self.cellsReachingPacific = []
        self.cellsReachingAtlantic = []
        
    def isValid(self, row, col, matrix, previousValue):
        if (row >= 0 and row < len(matrix)):
            if (col >=0 and col < len(matrix[0])):
                if (matrix[row][col] <= previousValue):
                    return True
        return False
    
    def nextMove(self, row, col, matrix):
        moves = []
        # up
        if (self.isValid(row-1, col, matrix, matrix[row][col])):
            moves.append([row-1, col])
        # left
        if (self.isValid(row, col-1, matrix, matrix[row][col])):
            moves.append([row, col-1])
        # down
        if (self.isValid(row+1, col, matrix, matrix[row][col])):
            moves.append([row+1, col])
        # right
        if (self.isValid(row, col+1, matrix, matrix[row][col])):
            moves.append([row, col+1])
        return moves
    
    def canReachPacific(self, row, col, matrix, visited):
        # by adding row, col to cellsReachingPacific we avoid extra work of traversing the previously travelled path again.FloatingPointError
        if ([row, col] in self.cellsReachingPacific):
            return True
        if (row == 0 or col == 0):
            return True
        # Mark current cell visited
        visited.append([row, col])
        # get the next moves
        nextMoves = self.nextMove(row, col, matrix)
        for move in nextMoves:
            if (move not in visited):
                if (self.canReachPacific(move[0], move[1], matrix, visited)):
                    self.cellsReachingPacific.append([row, col])
                    return True
    
    def canReachAtlantic(self, row, col, matrix, visited):
        # by adding row, col to cellsReachingAtlantic we avoid extra work of traversing the previously travelled path again.FloatingPointError
        if ([row, col] in self.cellsReachingAtlantic):
            return True
        if (row == len(matrix)-1 or col == len(matrix[0])-1):
            return True
        # Mark current cell visited
        visited.append([row, col])
        # get the next moves
        nextMoves = self.nextMove(row, col, matrix)
        for move in nextMoves:
            if (move not in visited):
                if (self.canReachAtlantic(move[0], move[1], matrix, visited)):
                    self.cellsReachingAtlantic.append([row, col])
                    return True
        
    def pacificAtlantic(self, heights):
        cells = []
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if (self.canReachPacific(row, col, heights, []) and self.canReachAtlantic(row, col, heights, [])):
                    cells.append([row, col])
        return cells
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        

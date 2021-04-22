# Max Area of Island
# https://leetcode.com/problems/max-area-of-island/
class Solution(object):
    def __init__(self):
        self.maxSize = 0
    
    def isValid(self, row, col, grid):
        if (row >= 0 and row < len(grid)):
            if (col >= 0 and col < len(grid[0])):
                if (grid[row][col] == 1):
                    return True
        return False
    
    def nextValidMoves(self, row, col, grid):
        moves = []
        # up
        if (self.isValid(row-1, col, grid)):
            moves.append([row-1, col])
        # down
        if (self.isValid(row+1, col, grid)):
            moves.append([row+1, col])
        # left
        if (self.isValid(row, col-1, grid)):
            moves.append([row, col-1])
        # right
        if (self.isValid(row, col+1, grid)):
            moves.append([row, col+1])
        return moves
        
    def findIsland(self, row, col, grid, size):
        if (grid[row][col]==0):
            return
        print 'row',row, 'col',col
        # Mark current as visited
        grid[row][col] = 0
        # increment the size
        size[0] = size[0]+1
        # get the next moves
        moves = self.nextValidMoves(row, col, grid)
        for move in moves:
            self.findIsland(move[0], move[1], grid, size)
        
    def maxAreaOfIsland(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 1):
                    size = [0]
                    self.findIsland(row, col, grid, size)
                    self.maxSize = max(self.maxSize, size[0])
                    print size
        return self.maxSize
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        

#  Max Area of Island
# https://leetcode.com/problems/max-area-of-island/
class Solution(object):
    def isValid(self, row, col, grid):
        if (row >= 0 and row < len(grid)):
            if (col >= 0 and col < len(grid[0])):
                if (grid[row][col] == 1):
                    return True
        return False
    
    def nextMove(self, row, col, grid):
        #                 down.   up.     left.  right
        potentialMoves = [[1,0], [-1,0], [0,1], [0,-1]]
        moves = []
        for m in potentialMoves:
            if (self.isValid(row+m[0], col+m[1], grid)):
                moves.append([row+m[0], col+m[1]])
        return moves
    
    def visitIsland(self, row, col, grid, area):
        # add to area
        area[0] += 1
        # mark row, col visited
        grid[row][col] = 0
        # get next moves
        moves = self.nextMove(row, col, grid)
        # go through moves
        for m in moves:
            # don't visit already visited cell.
            if (grid[m[0]][m[1]] == 0):
                continue
            self.visitIsland(m[0], m[1], grid, area)
        
    def maxAreaOfIsland(self, grid):
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 1):
                    area = [0]
                    self.visitIsland(row, col, grid, area)
                    print area
                    maxArea = max(maxArea, area[0])
        return maxArea
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        

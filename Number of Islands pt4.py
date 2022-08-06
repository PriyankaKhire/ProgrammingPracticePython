# Number of Islands
# https://leetcode.com/problems/number-of-islands/
class Solution(object):
    def isValid(self, row, col, grid):
        if (row >= 0 and row < len(grid)):
            if (col >= 0 and col < len(grid[0])):
                if (grid[row][col] == "1"):
                    return True
        return False
    
    def nextMove(self, row, col, grid):
        moves = []
        # down
        if (self.isValid(row+1, col, grid)):
            moves.append([row+1, col])
        # up
        if (self.isValid(row-1, col, grid)):
            moves.append([row-1, col])
        # left 
        if (self.isValid(row, col+1, grid)):
            moves.append([row, col+1])
        # right
        if (self.isValid(row, col-1, grid)):
            moves.append([row, col-1])
        return moves
    
    def visitIsland(self, row, col, grid):
        # mark current row and col visited
        grid[row][col] = "0"
        # get next moves
        moves = self.nextMove(row, col, grid)
        for move in moves:
            self.visitIsland(move[0], move[1], grid)
        
    def numIslands(self, grid):
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == "1"):
                    self.visitIsland(row, col, grid)
                    count += 1
        return count
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        

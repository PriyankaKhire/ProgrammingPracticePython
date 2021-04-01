#Max Area of Island
# https://leetcode.com/problems/max-area-of-island/

class Solution(object):
    def isValid(self, row, col, grid):
        if (row >= 0 and row < len(grid)):
            if (col >= 0 and col < len(grid[0])):
                # if there is land there
                if (grid[row][col] == 1):
                    return True
        return False

    def addToMoves(self, row, col, grid, moves):
        if (self.isValid(row, col, grid)):
            moves.append([row, col])

    def nextMove(self, row, col, grid):
        moves = []
        # Up
        self.addToMoves(row-1, col, grid, moves)
        # Down
        self.addToMoves(row+1, col, grid, moves)
        # Left
        self.addToMoves(row, col-1, grid, moves)
        # Right
        self.addToMoves(row, col+1, grid, moves)
        return moves

    def dfs(self, row, col, grid, area):
        # If current's already been visited then don't visit it again
        if (grid[row][col] == 0):
            return
        # Mark current visited
        grid[row][col] = 0
        # Add to area
        area[0] = area[0] + 1
        # get next moves
        moves = self.nextMove(row, col, grid)
        # recurse
        for move in moves:
            self.dfs(move[0], move[1], grid, area)
        
    def maxAreaOfIsland(self, grid):
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if we find land
                if (grid[row][col] == 1):
                    area = [0]
                    self.dfs(row, col, grid, area)
                    maxArea = max(maxArea, area[0])
        print maxArea
        """
        :type grid: List[List[int]]
        :rtype: int
        """

# Main
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

obj = Solution()
obj.maxAreaOfIsland(grid)

grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]]

obj = Solution()
obj.maxAreaOfIsland(grid)

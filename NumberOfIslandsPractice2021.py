# Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def isValid(self, row, col, grid):
        if (row >= 0 and row < len(grid)):
            if (col >= 0 and col < len(grid[0])):
                # if there is land
                if (grid[row][col] == "1"):
                    return True
        return False

    def addNextMove(self, row, col, grid, moves):
        if (self.isValid(row, col, grid)):
            moves.append([row, col])
            
    def nextMove(self, row, col, grid):
        moves = []
        # Up
        self.addNextMove(row-1, col, grid, moves)
        # Down
        self.addNextMove(row+1, col, grid, moves)
        # Left
        self.addNextMove(row, col-1, grid, moves)
        # Right
        self.addNextMove(row, col+1, grid, moves)
        return moves

    def dfs(self, grid, row, col):
        # Mark current visited
        grid[row][col] = "0"
        # get adjacent lands
        moves = self.nextMove(row, col, grid)
        for move in moves:
            self.dfs(grid, move[0], move[1])
            
        
    def numIslands(self, grid):
        numberOfIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if we find beginning of an island
                if (grid[row][col] == "1"):
                    numberOfIslands = numberOfIslands + 1
                    # Mark island visited
                    self.dfs(grid, row, col)
        print "Total number of islands are", numberOfIslands
        """
        :type grid: List[List[str]]
        :rtype: int
        """

# Main
grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
obj = Solution()
obj.numIslands(grid1)

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
obj = Solution()
obj.numIslands(grid2)

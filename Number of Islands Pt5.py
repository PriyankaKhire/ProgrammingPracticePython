# Number of Islands
# https://leetcode.com/problems/number-of-islands/description

class Solution(object):
    def isValid(self, grid, row, col):
        if (row >= 0 and row < len(grid)):
            if (col >=0 and col < len(grid[0])):
                if (grid[row][col] == "1"):
                    return True
        return False

    def liquifyIsland(self, grid, row, col):
        # Liquify the current row and col
        grid[row][col] = "0"
        # search up
        if (self.isValid(grid, row-1, col)):
            self.liquifyIsland(grid, row-1, col)
        # search down
        if (self.isValid(grid, row+1, col)):
            self.liquifyIsland(grid, row+1, col)
        # search left
        if (self.isValid(grid, row, col-1)):
            self.liquifyIsland(grid, row, col-1)
        # search right
        if (self.isValid(grid, row, col+1)):
            self.liquifyIsland(grid, row, col+1)

    def numIslands(self, grid):
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == "1"):
                    self.liquifyIsland(grid, row, col)
                    count += 1
        return count
        """
        :type grid: List[List[str]]
        :rtype: int
        """

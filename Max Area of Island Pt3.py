# Max Area of Island
# https://leetcode.com/problems/max-area-of-island/description/

class Solution(object):
    def isValid(self, row, col, grid):
        if (row >= 0 and row < len(grid)):
            if (col >= 0 and col < len(grid[0])):
                if (grid[row][col] == 1):
                    return True
        return False

    def nextMove(self, row, col, grid):
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        nextMovesArray = []
        for m in moves:
            if (self.isValid(row + m[0], col + m[1], grid)):
                nextMovesArray.append([row + m[0], col + m[1]])
        return nextMovesArray

    def display(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                print grid[row][col],
            print ""

    def areaOfIsland(self, grid, row, col, area):
        # add to area
        area[0] += 1
        # Mark the current row, col, visited
        grid[row][col] = 0
        # get next moves
        moves = self.nextMove(row, col, grid)
        for m in moves:
            # is current cell is not visited, this can happen while backtracking
            if (self.isValid(m[0], m[1], grid)):
                self.areaOfIsland(grid, m[0], m[1], area)
            # "backtrack"

    def maxAreaOfIsland(self, grid):
        maxArea = 0
        area = [0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 1):
                    area = [0]
                    self.areaOfIsland(grid, row, col, area)
                    maxArea = max(maxArea, area[0])
        return maxArea
        """
        :type grid: List[List[int]]
        :rtype: int
        """

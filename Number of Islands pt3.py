#Number of Islands
#https://leetcode.com/problems/number-of-islands/
class Solution(object):
    def isValid(self, row, col, grid):
        if(row >= 0 and row < len(grid)):
            if(col >= 0 and col < len(grid[0])):
                return True
        return False
    
    def dfs(self, row, col, grid):
        grid[row][col] = 0
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for neighbor in neighbors:
            nRow = row+neighbor[0]
            nCol = col+neighbor[1]
            if(self.isValid(nRow, nCol, grid) and grid[nRow][nCol] == 1):
                self.dfs(nRow, nCol, grid)
        
        
    def numIslands(self, grid):
        islandNumber = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == 1):
                    islandNumber = islandNumber + 1
                    self.dfs(row, col, grid)
        print islandNumber
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
#Main
grid1 = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0]
    ]
grid2 = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
    ]
grid3 = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
    ]
obj = Solution()
obj.numIslands(grid3)

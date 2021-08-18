# Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def isValid(self, row, col, matrix):
        if (row >= 0 and row < len(matrix)):
            if (col >= 0 and col < len(matrix[0])):
                if (matrix[row][col] == "1"):
                    return True
    
    def nextMove(self, row, col, matrix):
        moves = []
        # up
        if (self.isValid(row-1, col, matrix)):
            moves.append([row-1, col])
        # down
        if (self.isValid(row+1, col, matrix)):
            moves.append([row+1, col])
        # left
        if (self.isValid(row, col-1, matrix)):
            moves.append([row, col-1])
        # right
        if (self.isValid(row, col+1, matrix)):
            moves.append([row, col+1])
        return moves
    
    def dfs(self, row, col, matrix):
        # mark current row and col visited
        matrix[row][col] = "0"
        # find the next move
        moves = self.nextMove(row, col, matrix)
        # visit the adjacent cells
        for move in moves:
            if (matrix[move[0]][move[1]] == "1"):
                self.dfs(move[0], move[1], matrix)
        
    def numIslands(self, grid):
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == "1"):
                    self.dfs(row, col, grid)
                    count = count + 1
        return count
        """
        :type grid: List[List[str]]
        :rtype: int
        """

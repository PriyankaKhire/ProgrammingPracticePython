#Number of Islands
#https://leetcode.com/problems/number-of-islands/description/

class Solution(object):
    
    def isValid(self, row, col, matrix):
        if((row < len(matrix)) and (col < len(matrix[0]))):
            if((row >= 0) and (col >= 0)):
                if(matrix[row][col] == "1"):
                    return True
        return False
    
    def nextMove(self, row, col, matrix):
        moves = []
        #up
        if(self.isValid(row-1, col, matrix)):
            moves.append([row-1, col])
        #down
        if(self.isValid(row+1, col, matrix)):
            moves.append([row+1, col])
        #left
        if(self.isValid(row, col-1, matrix)):
            moves.append([row, col-1])
        #right
        if(self.isValid(row, col+1, matrix)):
            moves.append([row, col+1])
        return moves
    
    def dfs(self, matrix, row, col):
        #make current cell visited by marking it 0
        matrix[row][col] = 0
        moves = self.nextMove(row, col, matrix)
        for move in moves:
            r = move[0]
            c = move[1]
            if(self.isValid(r,c,matrix)):
                self.dfs(matrix, r, c)
        
    
    def numIslands(self, matrix):
        islandCount = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if(matrix[row][col] == "1"):
                    islandCount = islandCount+1
                    self.dfs(matrix, row, col)
        print islandCount
        
        """
        :type grid: List[List[str]]
        :rtype: int
        """

#Main Program
m = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
s = Solution()
s.numIslands(m)

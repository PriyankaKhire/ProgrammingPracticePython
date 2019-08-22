# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
class Solution(object):
    
    def initialEdgeCases(self, n):
        if(n==0):
            return 1
        if(n==1):
            return 1
        if(n==2):
            return 2
        return "None"
    
    def fillMatrix(self, n):
        matrix =[[0 for col in range(n+1)] for row in range(n+1)]
        row = 0
        col = 0
        startCol = 0
        while(startCol < n+1):
            if(row == col or col == row+1):
                matrix[row][col] = 1
            else:
                matrix[row][col] = matrix[row][col-1] + matrix[row+2][col]
            row = row+1
            col = col+1
            if(col == n+1):
                startCol = startCol+1
                row = 0
                col = startCol
        return matrix[0][n]
                
        
        
    def climbStairs(self, n):
        initial = self.initialEdgeCases(n)
        if(initial != "None"):
            return initial
        return self.fillMatrix(n)
        """
        :type n: int
        :rtype: int
        """

#Unique Paths
#https://leetcode.com/problems/unique-paths/

class Solution(object):
    
    def fillMatrix(self, matrix):
        #fill first row
        for col in range(0, len(matrix[0])):
            matrix[0][col] = 1
        #fill first col
        for row in range(1, len(matrix)):
            matrix[row][0] = 1
        #fill rest of the matrix
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                matrix[row][col] = matrix[row-1][col] + matrix[row][col-1]
        return matrix[-1][-1]
        
    def uniquePaths(self, m, n):
        matrix = [[0 for col in range(m)] for row in range(n)]
        print "The number of unique paths for ",n," rows and ",m,"cols, from top left to bottom right are: ", self.fillMatrix(matrix)
        """
        :type m: int
        :type n: int
        :rtype: int
        """

#Main
obj1 = Solution()
obj1.uniquePaths(7, 3)

# Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setRowToX(self, row, matrix):
        for col in range(len(matrix[0])):
            if (matrix[row][col] != 0):
                matrix[row][col] = "x"
    
    def setColToX(self, col, matrix):
        for row in range(len(matrix)):
            if (matrix[row][col] != 0):
                matrix[row][col] = "x"
    
    def setToZero(self, matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (matrix[row][col] == "x"):
                    matrix[row][col] = 0
                
    def setZeroes(self, matrix):
        # set row and col of the cell that has 0 to x
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (matrix[row][col] == 0):
                    self.setRowToX(row, matrix)
                    self.setColToX(col, matrix)
                    
        # set the negative numbers to zero
        self.setToZero(matrix)
        
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        

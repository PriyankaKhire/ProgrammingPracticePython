# Rotate Image
# https://leetcode.com/problems/rotate-image/

class Solution(object):
    def diagonalSwap(self, matrix):
        colBound = 0
        rowBound = 0
        # extra minus one is from preventing the diagonal getting swapped
        while(rowBound < len(matrix)-1):
            # swap cells, we wanna swap row, col with len-1-col, len-1-row
            matrix[rowBound][colBound], matrix[len(matrix[0])-1-colBound][len(matrix)-1-rowBound] = matrix[len(matrix[0])-1-colBound][len(matrix)-1-rowBound], matrix[rowBound][colBound]
            # increment the col value
            colBound = colBound + 1
            # extra minus row bound is from preventing the diagonal from getting swapped.
            if (colBound == len(matrix[0])-1-rowBound):
                colBound = 0
                rowBound = rowBound + 1
    
    def inverseMatrix(self, matrix):
        for row in range(len(matrix)/2):
            # swap first row with last
            matrix[row], matrix[len(matrix)-1-row] = matrix[len(matrix)-1-row], matrix[row]
                
    def rotate(self, matrix):
        self.diagonalSwap(matrix)
        self.inverseMatrix(matrix)
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        

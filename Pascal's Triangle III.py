# Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/
class Solution(object):
    def logic(self, numRows, row, triangle):
        if (row == numRows):
            return
        for col in range(row+1):
            if (col == 0 or col == row):
                triangle[row].append(1)
            else:
                #append sum of previosu row and col-1 and col above it
                triangle[row].append(triangle[row-1][col-1] + triangle[row-1][col])
        self.logic(numRows, row+1, triangle)
        
    def generate(self, numRows):
        triangle = [[] for row in range(numRows)]
        self.logic(numRows, 0, triangle)
        return triangle
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        

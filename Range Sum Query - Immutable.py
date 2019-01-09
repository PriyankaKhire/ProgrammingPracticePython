#Range Sum Query - Immutable
#https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        self.matrix = [[0 for col in range(len(nums))] for row in range(len(nums))]
        self.fillMatrix()
        """
        :type nums: List[int]
        """
    def fillMatrix(self):
        row = 0
        col = 0
        colStart = 0
        while(colStart < len(self.nums)):
            if(row == col):
                self.matrix[row][col] = self.nums[col]
            else:
                self.matrix[row][col] = self.matrix[row][col-1] + self.nums[col]
            col = col+1
            if(col == len(self.nums)):
                row = row+1
                colStart = colStart+1
                col = colStart
                
    def sumRange(self, i, j):
        print self.matrix[i][j]
        """
        :type i: int
        :type j: int
        :rtype: int
        """

#Main
obj = NumArray([-2, 0, 3, -5, 2, -1])
obj.sumRange(0, 2)
obj.sumRange(2, 5)
obj.sumRange(0, 5)

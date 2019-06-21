#Maximum Subarray
#https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def fillMatrix(self, nums, matrix):
        maxSum = nums[0]
        row = 0
        col = 0
        while(row < len(nums)):
            if(row == col):
                matrix[row][col] = nums[row]
            else:
                matrix[row][col] = matrix[row][col-1] + nums[col]
            maxSum = max(maxSum, matrix[row][col])
            col = col+1
            if(col == len(nums)):
                row = row+1
                col = row
        return maxSum
    def maxSubArray(self, nums):
        matrix = [[0 for col in range(len(nums))] for row in range(len(nums))]
        return self.fillMatrix(nums, matrix)
        """
        :type nums: List[int]
        :rtype: int
        """
        

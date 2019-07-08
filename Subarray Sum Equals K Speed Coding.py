#Subarray Sum Equals K
#https://leetcode.com/problems/subarray-sum-equals-k/
class Solution(object):
    def __init__(self):
        self.matrix = None
    
    def fillMatrix(self, nums, k):
        subArray = 0
        for row in range(len(nums)):
            for col in range(row, len(nums)):
                if(row == col):
                    self.matrix[row][col] = nums[col]
                else:
                    self.matrix[row][col] = self.matrix[row][col-1]+nums[col]
                if(self.matrix[row][col] == k):
                    subArray = subArray + 1
        return subArray
        
    def subarraySum(self, nums, k):
        self.matrix = [[0 for col in range(len(nums))] for row in range(len(nums))]
        return self.fillMatrix(nums, k)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

#Find Peak Element
#https://leetcode.com/problems/find-peak-element
class Solution(object):
    def findPeakElement(self, nums):
        if(len(nums) <= 1):
            return 0
        for i in range(len(nums)):
            if(i+1 < len(nums) and i == 0 and nums[i] > nums[i+1]):
                return i
            if(i+1 < len(nums) and nums[i] > nums[i+1] and nums[i] > nums[i-1]):
                return i
            if(i+1 == len(nums) and nums[i] > nums[i-1]):
                return i
        """
        :type nums: List[int]
        :rtype: int
        """
        

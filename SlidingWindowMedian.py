# Sliding Window Median
# https://leetcode.com/problems/sliding-window-median/

class Solution(object):
    def getMedian(self, nums):
        nums = sorted(nums)
        # if K is even
        if (len(nums)%2 == 0):
            return (nums[len(nums)/2] + nums[(len(nums)/2)-1])/float(2)
        return nums[len(nums)/2]
            
        
    def medianSlidingWindow(self, nums, k):
        answer = []
        for i in range(len(nums)-(k-1)):
            median = self.getMedian(nums[i:i+k])
            answer.append(median)
        return answer
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        

# Minimum length consecutive subarray sum
'''
Find the minimum length of consecutive sub array whose sum equals target.

Example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The consecutive subarray [4,3] has the minimal length under the problem constraint.
Even though the consecutive subarray [1,2,4] also sums to target it has more elements
'''

class Solution(object):
    def findWindowSum(self, target, nums, windowStart, windowEnd, windowSum, elementCount):
        minElementCount = len(nums)+1
        while (windowEnd+1 < len(nums) and windowStart < len(nums)):
            if (windowSum == target):
                minElementCount = min(elementCount, minElementCount)
            # start the window
            windowEnd += 1
            windowSum += nums[windowEnd]
            elementCount += 1
            # decrease the window
            while (windowSum > target):
                windowSum -= nums[windowStart]
                elementCount -= 1
                windowStart += 1
        # check one last time if remaining window sum is equal to target or not.
        if (windowSum == target):
            minElementCount = min(elementCount, minElementCount)
        if (minElementCount > len(nums)):
            return 0
        return minElementCount

    def minSubArrayLen(self, target, nums):
        if (len(nums) == 1):
            if (nums[0] == target):
                return 1
            return 0
        elementCount = self.findWindowSum(target, nums, 0, 0, nums[0], 1)
        return elementCount
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
class Solution(object):

    # returns true if all elements in array are negative
    def ifAllNegative(self, nums):
        for num in nums:
            if (num > 0):
                return False
        return True
    
    def maxSubArray(self, nums):
        # if all elements in array are negative then return the largest of them all.
        if(self.ifAllNegative(nums)):
            return max(nums)
        # else this is the easy variation of kadnane's algo.
        # first initialize maxEndingHere with all 0s.
        maxEndingHere = [0 for i in range(len(nums))]
        # we don't want it if its a -ve number
        if(nums[0] > 0):
            maxEndingHere[0] = nums[0]
        for i in range(1, len(nums)):
            if(maxEndingHere[i-1]+nums[i] > 0):
                maxEndingHere[i] = maxEndingHere[i-1]+nums[i]
        print maxEndingHere
        print "The max sum sub array is", max(maxEndingHere)
        """
        :type nums: List[int]
        :rtype: int
        """

# Main
obj = Solution()
obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

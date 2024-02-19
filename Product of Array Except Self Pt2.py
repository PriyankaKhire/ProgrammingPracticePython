# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelf(self, nums):
        leftToRight = [0 for i in range(len(nums))]
        leftToRight[0] = nums[0]
        # get product from left to right
        for i in range(1, len(nums)):
            leftToRight[i] = nums[i] * leftToRight[i - 1]
        rightToLeft = [0 for i in range(len(nums))]
        rightToLeft[-1] = nums[-1]
        # get product from right to left
        for i in range(len(nums) - 2, -1, -1):
            rightToLeft[i] = nums[i] * rightToLeft[i + 1]
        # get the output
        output = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if (i - 1 < 0):
                output[i] = rightToLeft[i + 1]
            elif (i + 1 == len(nums)):
                output[i] = leftToRight[i - 1]
            else:
                output[i] = leftToRight[i - 1] * rightToLeft[i + 1]
        return output
        """
        :type nums: List[int]
        :rtype: List[int]
        """

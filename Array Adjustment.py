#Array Adjustment
'''
Given an integer array nums containing positive elements and an int maxValue.
Find the value of x such that the sum of the elements of the array is maximum
and is less than the given maxValue.
x is defined as: if the current value is greater than x, then x is used as the new value,
otherwise keep the original value nums[i] = min(x, nums[i]).

Example 1:

Input: nums = [10, 5, 20, 30], maxValue = 40
Output: 12
Explanation:
If x = 10, the array would be nums = [10, 5, 10, 10] and the sum of the array elements would be 35.
If x = 12, the array would be nums = [10, 5, 12, 12] and the sum of the elements would be 39 which is the maximum sum close to given maxValue which is 40.
So the answer would be 12.
'''
class Solution(object):
    def __init__(self):
        self.largestX = None
        
    def getNewAdjustedArray(self, nums, x):
        newArray = []
        for num in nums:
            newArray.append(min(x, num))
        return newArray

    def binarySearch(self, nums, maxValue, low, high):
        if(low > high):
            return
        mid = (low+high)/2
        newArray = self.getNewAdjustedArray(nums, mid)
        if(sum(newArray) >= maxValue):
            self.binarySearch(nums, maxValue, low, mid-1)
        else:
            # Record the mid value as highest x value
            self.largestX = mid
            self.binarySearch(nums, maxValue, mid+1, high)
        
    def getX(self, nums, maxValue):
        # From the problem we see that there is a range here,
        # at any given point we cannot change value of x to be more than the largest element
        # because of this rule nums[i] = min(x, nums[i]).
        for x in range(1, max(nums)):
            newArray = self.getNewAdjustedArray(nums, x)
            print newArray, sum(newArray)
        # from the above output we see that we can use binary search here.
        self.binarySearch(nums, maxValue, 1, max(nums))
        print self.largestX

# Main
nums = [10, 5, 20, 30]
maxValue = 40
obj = Solution()
obj.getX(nums, maxValue)

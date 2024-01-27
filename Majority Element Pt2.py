# Majority Element
# https://leetcode.com/problems/majority-element/description

class Solution(object):
    def majorityElement(self, nums):
        # sort the array
        nums.sort()
        # count the occurrences of the elements using window approach
        ptr = 0
        while (ptr < len(nums)):
            count = 1
            while(ptr+count < len(nums) and nums[ptr] == nums[ptr+count]):
                count += 1
            if (count > len(nums)/2):
                return nums[ptr]
            ptr += count
        """
        :type nums: List[int]
        :rtype: int
        """

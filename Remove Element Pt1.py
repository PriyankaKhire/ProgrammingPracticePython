# Remove Element
# https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        # Replace all elements that are equal to Val with last elements from array
        j = len(nums) - 1
        # count the occourances of val
        count = 0
        for i in range(len(nums)):
            if (nums[i] != val):
                continue
            count += 1
            while (i < j and nums[j] == val):
                j -= 1
            if (i < j):
                nums[i] = nums [j]
                j -= 1
        return len(nums) - count
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        

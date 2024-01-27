# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description

class Solution(object):
    def removeDuplicates(self, nums):
        # Replace duplicates with _
        ptr = 0
        while(ptr < len(nums)-1):
            windowEnd = ptr +1
            while(windowEnd < len(nums) and nums[ptr] == nums[windowEnd]):
                nums[windowEnd] = "_"
                windowEnd += 1
            ptr = windowEnd 
        # move all the numbers to the front
        numsPtr = 0
        emptySpacePtr = None
        while (numsPtr < len(nums)):
            # Find the first empty space
            if (not emptySpacePtr and nums[numsPtr] == "_"):
                emptySpacePtr = numsPtr
            if (emptySpacePtr and nums[numsPtr] != "_"):
                nums[emptySpacePtr] = nums[numsPtr]
                nums[numsPtr] = "_"
                emptySpacePtr += 1
            numsPtr += 1
        return emptySpacePtr
        """
        :type nums: List[int]
        :rtype: int
        """

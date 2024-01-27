# Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description

class Solution(object):
    def removeDuplicates(self, nums):
        # replace duplicate elements with _ but make sure we leave 2 copies of 1 element
        ptr = 0
        while (ptr < len(nums)-1):
            windowEnd = ptr
            uniqueCount = 0
            while (windowEnd < len(nums) and nums[ptr] == nums[windowEnd]):
                if (uniqueCount < 2):
                    uniqueCount += 1
                else:
                    nums[windowEnd] = "_"
                windowEnd += 1
            ptr = windowEnd
        # pull all the numbers close together
        emptySpace = None
        for i in range(len(nums)):
            # find the first empty space
            if (not emptySpace and nums[i] == "_"):
                emptySpace = i
                continue
            if (emptySpace and nums[i] != "_"):
                nums[emptySpace] = nums[i]
                nums[i] = "_"
                emptySpace += 1
        return emptySpace
        """
        :type nums: List[int]
        :rtype: int
        """

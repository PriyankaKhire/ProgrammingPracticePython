# Remove Element
# https://leetcode.com/problems/remove-element/description/
class Solution(object):
    def removeElement(self, nums, val):
        # Remove the element and replace it with _ also count the element that are not equal to val
        count = 0
        for i in range(len(nums)):
            if (nums[i] == val):
                nums[i] = '_'
            else:
                count += 1
        # not have start ptr and end ptr
        startPtr = 0
        endPtr = len(nums) - 1
        while (startPtr < endPtr):
            if (nums[endPtr] == "_"):
                endPtr -= 1
                continue
            if (nums[startPtr] != "_"):
                startPtr += 1
                continue
            # at this point the endPtr is pointing to a number and startPtr is pointing to _
            nums[startPtr] = nums[endPtr]
            # this is just so array looks neat, this code line is not needed
            nums[endPtr] = "_"
            startPtr += 1
            endPtr -= 1
        return count
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def sortingApproach(self, nums):
        # sort the numbers
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if (nums[i] == nums[i + 1]):
                return True
        return False

    def hashTableApproach(self, nums):
        hashTable = {}
        for n in nums:
            if (n not in hashTable):
                hashTable[n] = True
                continue
            return True
        return False

    def containsDuplicate(self, nums):
        # return self.hashTableApproach(nums)
        return self.sortingApproach(nums)
        """
        :type nums: List[int]
        :rtype: bool
        """

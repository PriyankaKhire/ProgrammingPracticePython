# Two Sum
# https://leetcode.com/problems/two-sum/description/

class Solution(object):

    # the sorting approach doens't work because you have to return indices and not the numbers themselves.
    def sortingApproach(self, nums, target):
        # sort the array
        nums = sorted(nums)
        # have 2 pointers
        start = 0
        end = len(nums) - 1
        while (start < end):
            currSum = nums[start] + nums[end]
            print "Current sum", currSum
            if (currSum == target):
                return [start, end]
            if (currSum > target):
                end -= 1
            if (currSum < target):
                start += 1

    def hashTableApproach(self, nums, target):
        # key = number, value = [list of indices]
        hashTable = {}
        # put numbers and indices in hash table
        for i in range(len(nums)):
            n = nums[i]
            if (n not in hashTable):
                hashTable[n] = []
            hashTable[n].append(i)
        print hashTable
        # for every number check if target - number is present in hash table or not
        for key in hashTable:
            print "key", key,
            otherNum = target - key
            print "other num", otherNum
            if (otherNum == key):
                # this is for cases like 3, 3 and target is 6
                if (len(hashTable[key]) >= 2):
                    return [hashTable[key][0], hashTable[key][1]]
            else:
                # if we can find other number in hash table
                if (otherNum in hashTable):
                    return [hashTable[key][0], hashTable[otherNum][0]]

    def twoSum(self, nums, target):
        return self.hashTableApproach(nums, target)
        # return self.sortingApproach(nums, target)
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

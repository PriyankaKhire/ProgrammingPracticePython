# Two Sum
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def addToHashAndSeeSum(self, nums, target):
        hashTable = {}
        for i in range(len(nums)):
            # if hash table not empty
            if hashTable:
                # find if hash table has target
                # remember it's target - nums[i] because target is sum of 2 numbers hence it will always be greater than the two numbers in question.
                if (target-nums[i] in hashTable):
                    return [i, hashTable[target-nums[i]][0]]
            # add number to hash table
            if (nums[i] not in hashTable):
                hashTable[nums[i]] = []
            hashTable[nums[i]].append(i)
                
    def twoSum(self, nums, target):
        return self.addToHashAndSeeSum(nums, target)
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

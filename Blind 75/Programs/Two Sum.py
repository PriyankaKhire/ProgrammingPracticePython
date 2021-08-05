# Two Sum
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def addToHashTable(self, nums):
        hashTable = {}
        for i in range(len(nums)):
            if (nums[i] not in hashTable):
                hashTable[nums[i]] = []
            hashTable[nums[i]].append(i)
        return hashTable
    
    def twoSum(self, nums, target):
        # Add nums to hash table
        hashTable = self.addToHashTable(nums)
        # Check if the difference exists in hashTable
        for i in range(len(nums)):
            difference = (target-nums[i])
            # if the difference is present in hash table
            if (difference in hashTable):
                # if the number wanted and current number is same.
                if(difference == nums[i]):
                    # how ever we need to check for the length of the array.
                    # what if there is a case like [3, 4, 2] target = 6
                    # then 3 might be counted in twice.
                    if (len(hashTable[difference]) >= 2):
                        # only if the length is greater than or equal to 2
                        return hashTable[difference]
                else:
                    # else if the numbers are not the same then we just return their indices.
                    return [i, hashTable[difference][0]]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

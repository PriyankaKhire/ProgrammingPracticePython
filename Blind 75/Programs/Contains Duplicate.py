# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def __init__(self):
        self.hashMap = {}
        
    def addToMap(self, nums):
        for i in range(len(nums)):
            if(nums[i] not in self.hashMap):
                self.hashMap[nums[i]] = True
            else:
                return True
        return False
    
    def containsDuplicate(self, nums):
        return self.addToMap(nums)
        """
        :type nums: List[int]
        :rtype: bool
        """
        

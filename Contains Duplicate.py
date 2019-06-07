#Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/
class HashTable(object):
    def __init__(self):
        self.hashTable = {}

    def logic(self, nums):
        for num in nums:
            if not(num in self.hashTable):
                self.hashTable[num] = True
            else:
                return True
        return False
    
    def containsDuplicate(self, nums):
        print self.logic(nums)
        """
        :type nums: List[int]
        :rtype: bool
        """
class Sorting(object):
    def logic(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True
        return False
        
    def containsDuplicate(self, nums):
        print self.logic(nums)

#Main
obj = HashTable()
obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2])

obj = HashTable()
obj.containsDuplicate([1,2,3,4])

obj = Sorting()
obj.containsDuplicate([1,1,1,3,3,4,3,2,4,2])

obj = Sorting()
obj.containsDuplicate([1,2,3,4])

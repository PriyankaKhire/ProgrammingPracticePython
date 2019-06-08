#Contains Duplicate II
#https://leetcode.com/problems/contains-duplicate-ii/
class Solution(object):
    def logic(self, nums, k):
        hashTable = {}
        for i in range(len(nums)):
            if not(nums[i] in hashTable):
                hashTable[nums[i]] = [i]
            else:
                for index in hashTable[nums[i]]:
                    if(i-index <= k):
                        return True
                hashTable[nums[i]].append(i)
        return False
    
    def containsNearbyDuplicate(self, nums, k):
        print self.logic(nums, k)
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
#Main
obj = Solution()
obj.containsNearbyDuplicate([1,2,3,1], 3)

obj = Solution()
obj.containsNearbyDuplicate([1,0,1,1], 1)

obj = Solution()
obj.containsNearbyDuplicate([1,2,3,1,2,3], 2)

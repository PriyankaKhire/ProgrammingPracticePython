#Contains Duplicate III
#https://leetcode.com/problems/contains-duplicate-iii/
class Solution(object):
    def isValid(self, index, nums):
        if(index >= 0):
            if(index < len(nums)):
                return True
        return False
    
    def logic(self, nums, k, t):
        for i in range(len(nums)):
            #print "I ", i, " nums[i] ", nums[i]
            for j in range(1, k+1):
                #print "j ", j, " i-j ", i-j, " i+j ", i+j
                if(self.isValid(i-j, nums) and abs(nums[i]-nums[i-j]) <= t):
                    return True
                if(self.isValid(i+j, nums) and abs(nums[i]-nums[i+j]) <= t):
                    return True
        return False
            
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        print self.logic(nums, k, t)
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
#Main
obj = Solution()
obj.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2)

obj = Solution()
obj.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0)

obj = Solution()
obj.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3)

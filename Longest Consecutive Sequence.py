#Longest Consecutive Sequence
#https://leetcode.com/problems/longest-consecutive-sequence/description/
class Solution(object):
    def __init__(self):
        self.hash = {}

    def insertInHash(self, nums):
        for n in nums:
            if not(n in self.hash):
                self.hash[n] = 1
            else:
                self.hash[n] = self.hash[n] + 1

    def findSequence(self, nums):
        maxCount = 0
        count = 0
        for i in range(len(nums)):
            n = nums[i]
            while(n in self.hash):
                n = n+1
                count = count+1
            if(count > maxCount):
                maxCount = count
            count = 0
        return maxCount
    
    def longestConsecutive(self, nums):
        self.insertInHash(nums)
        print self.findSequence(nums)
        """
        :type nums: List[int]
        :rtype: int
        """

#Main
o = Solution()
o.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])

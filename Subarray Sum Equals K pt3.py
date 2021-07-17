# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution(object):
        
    def subarraySum(self, nums, k):
        numArray = 0
        for i in range(len(nums)):
            print "Starting from index i",i
            totalSum = 0
            j = 0
            while(i+j < len(nums)):
                print totalSum
                totalSum = totalSum + nums[i+j]
                if(totalSum == k):
                    numArray = numArray + 1
                j = j+1
        return numArray
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        

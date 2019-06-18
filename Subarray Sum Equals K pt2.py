#Subarray Sum Equals K
#https://leetcode.com/problems/subarray-sum-equals-k/
class Solution(object):
    def __init__(self):
        self.intermediateSum = []
    
    def calculateIntermediateSum(self, nums): 
        self.intermediateSum.append(nums[0])
        for i in range(1, len(nums)):
            self.intermediateSum.append(self.intermediateSum[i-1]+nums[i])
        #print self.intermediateSum
    
    def findSubArrays(self, nums, k):
        output = 0
        for i in range(len(nums)):
            j = 0
            s = 0
            while(j <= i):
                if(j == i):
                    s = nums[i]
                elif(j == 0):
                    s = self.intermediateSum[i]
                else:
                    s = self.intermediateSum[i] - self.intermediateSum[j-1]
                if(s == k):
                    output = output+1
                j = j+1
        return output
                     
    def subarraySum(self, nums, k):
        self.calculateIntermediateSum(nums)
        return self.findSubArrays(nums, k)
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

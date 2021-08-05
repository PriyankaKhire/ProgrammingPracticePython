# 3Sum
# https://leetcode.com/problems/3sum/

class Solution(object):
        
    def threeSum(self, nums):
        answers = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (i != j and i != k and j != k):
                        if (nums[i]+nums[j]+nums[k] == 0):
                            answer = sorted([nums[i], nums[j], nums[k]])
                            if (answer not in answers):
                                answers.append(answer)
        return answers      
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        

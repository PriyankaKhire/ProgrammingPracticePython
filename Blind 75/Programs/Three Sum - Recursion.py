# 3Sum
# https://leetcode.com/problems/3sum/

class Solution(object):
    def recurse(self, nums, indices, listOfAnswer):
        if (len(indices) == 3):
            if (nums[indices[0]] + nums[indices[1]] + nums[indices[2]] == 0):
                answer = sorted([nums[indices[0]], nums[indices[1]], nums[indices[2]]])
                if (answer not in listOfAnswer):
                    listOfAnswer.append(answer)
            return
        for i in range(len(nums)):
            if (i not in indices):
                self.recurse(nums, indices+[i], listOfAnswer)
        
    def threeSum(self, nums):
        listOfAnswer = []
        self.recurse(nums, [], listOfAnswer)
        return listOfAnswer
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        

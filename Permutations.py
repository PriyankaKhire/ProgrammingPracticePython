# Permutations
# https://leetcode.com/problems/permutations/

class Solution(object):
    
    def logic(self, nums, answer, visited, finalAnswer):
        if (len(answer) == len(nums)):
            finalAnswer.append(answer)
            return
        for i in range(len(visited)):
            if (visited[i] == False):
                visited[i] = True
                self.logic(nums, answer+[nums[i]], visited, finalAnswer)
                visited[i] = False
        
    def permute(self, nums):
        finalAnswer = []
        self.logic(nums, [], [False for i in range(len(nums))], finalAnswer)
        return finalAnswer
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        

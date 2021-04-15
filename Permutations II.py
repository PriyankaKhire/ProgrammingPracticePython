# Permutations II
# https://leetcode.com/problems/permutations-ii/

class Solution(object):
    def logic(self, nums, answer, visited, finalAnswer):
        if (len(answer) == len(nums)):
            if (answer not in finalAnswer):
                finalAnswer.append(answer)
            return
        for i in range(len(visited)):
            if(visited[i] == False):
                visited[i] = True
                self.logic(nums, answer+[nums[i]], visited, finalAnswer)
                # Backtrack
                visited[i] = False
                
    def permuteUnique(self, nums):
        finalAnswer = []
        self.logic(nums, [], [False for i in range(len(nums))], finalAnswer)
        return finalAnswer
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        

# Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

class Solution(object):
    def combinations(self, candidates, target, combos, index, answer):
        if(sum(combos) == target):
            combos.sort()
            if not(combos in answer):
                answer.append(combos)
            return
        for i in range(index, len(candidates)):
            self.combinations(candidates, target, combos+[candidates[i]], i+1, answer)
            
    def combinationSum2(self, candidates, target):
        answer = []
        self.combinations(candidates, target, [], 0, answer)
        return answer
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        

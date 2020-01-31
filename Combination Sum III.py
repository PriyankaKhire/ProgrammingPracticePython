# Combination Sum III
# https://leetcode.com/problems/combination-sum-iii/

class Solution(object):
    def combinaitons(self, k, n, combo, index, answer):
        if(len(combo) == k and sum(combo) == n):
            answer.append(combo)
            return
        for i in range(index, 10):
            self.combinaitons(k, n, combo+[i], i+1, answer)
            
    def combinationSum3(self, k, n):
        answer = []
        self.combinaitons(k, n, [], 1, answer)
        return answer
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        

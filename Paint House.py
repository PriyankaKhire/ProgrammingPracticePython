# Paint House
# https://leetcode.com/problems/paint-house/
class Solution(object):
    def backtrack(self, costs, totalCost, index, prevIndex, finalAnswer):
        if(index == len(costs)):
            finalAnswer[0] = min(totalCost, finalAnswer[0])
            return
        for i in range(len(costs[0])):
            if(i != prevIndex):
                self.backtrack(costs, totalCost+costs[index][i], index+1, i, finalAnswer)
            
    def minCost(self, costs):
        finalAnswer = [float('inf')]
        self.backtrack(costs, 0, 0, -1, finalAnswer)
        return finalAnswer[0]
        """
        :type costs: List[List[int]]
        :rtype: int
        """

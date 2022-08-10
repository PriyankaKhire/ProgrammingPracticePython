# Two City Scheduling
# https://leetcode.com/problems/two-city-scheduling/
class Solution(object):
    
    def recursion(self, costs, i, totalCost, flyingToA, flyingToB, minCost):
        if (i == len(costs) and flyingToA == flyingToB == len(costs)/2):
            minCost[0] = min(minCost[0], totalCost)
            return
        for index in range(i, len(costs)):
            # fly to city A
            if (flyingToA < len(costs)/2):
                self.recursion(costs, index+1, totalCost+costs[index][0], flyingToA+1, flyingToB, minCost)
            # fly to city B
            self.recursion(costs, index+1, totalCost+costs[index][1], flyingToA, flyingToB+1, minCost)
            
    def twoCitySchedCost(self, costs):
        minCost = [float('inf')]
        self.recursion(costs, 0, 0, 0, 0, minCost)
        return minCost[0]
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        

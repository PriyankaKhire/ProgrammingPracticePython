# Two City Scheduling
# https://leetcode.com/problems/two-city-scheduling/

class Solution(object):
            
    def twoCitySchedCost(self, costs):
        # list containing aCost-bCost
        abCost = []
        # gather the costs along with indices of the people
        for i in range(len(costs)):
            abCost.append([costs[i][0] - costs[i][1], i])
        # sort them according to lowest aCost-bCost
        abCost.sort(key=lambda x:x[0])
        # send first len(costs)/2 to fly to city a and rest to city b
        flyToA = {}
        # add the indices of employees that are flying to city A and city B
        for i in range(len(costs)):
            if (len(flyToA) < len(costs)/2):
                flyToA[abCost[i][1]] = True
        # compute the cost.
        totalCost = 0
        for i in range(len(costs)):
            if (i in flyToA):
                # send ith employee to city A
                totalCost += costs[i][0]
            else:
                # else send them to city B
                totalCost += costs[i][1]
        return totalCost
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        

# Buildings With an Ocean View
# https://leetcode.com/problems/buildings-with-an-ocean-view/

class Solution(object):
    def findBuildings(self, heights):
        indices = []
        maxHeightToRight = 0
        for i in range(len(heights)-1, -1, -1):
            if (heights[i] > maxHeightToRight):
                indices.append(i)
                maxHeightToRight = heights[i]
        indices.reverse()
        return indices
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        

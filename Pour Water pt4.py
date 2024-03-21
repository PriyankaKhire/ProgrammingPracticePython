# Pour Water
# https://leetcode.com/problems/pour-water/description/
class Solution(object):
    def goLeft(self, heights, k):
        currentHeight = k
        for h in range(k-1, -1, -1):
            if (heights[h] < heights[currentHeight]):
                currentHeight = h
                continue
            if (heights[h] > heights[currentHeight]):
                break
        if (currentHeight < k and heights[currentHeight] < heights[k]):
            heights[currentHeight] += 1
            return True
        return False
    
    def goRight(self, heights, k):
        currentHeight = k
        for h in range(k+1, len(heights)):
            if (heights[h] < heights[currentHeight]):
                currentHeight = h
                continue
            if (heights[h] > heights[currentHeight]):
                break
        if (currentHeight > k and heights[currentHeight] < heights[k]):
            heights[currentHeight] += 1
            return True
        return False

    def pourWater(self, heights, volume, k):
        for water in range(volume):
            if (self.goLeft(heights, k)):
                continue
            if (self.goRight(heights, k)):
                continue
            heights[k] += 1
        return heights
        """
        :type heights: List[int]
        :type volume: int
        :type k: int
        :rtype: List[int]
        """
        
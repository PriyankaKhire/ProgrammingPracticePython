# Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        largeLeft = [height[0]]
        for i in range(1,len(height)):
            largeLeft.append(max(height[i], largeLeft[-1]))
        largeRight = [height[-1]]
        for i in range(len(height)-2, -1, -1):
            largeRight.insert(0, max(largeRight[0], height[i]))
        #print largeRight
        #print largeLeft
        rainWaterTrapped = []
        for i in range(len(height)):
            if(i == 0 or i == len(height)-1):
                rainWaterTrapped.append(0)
                continue
            maxRainWaterYouCanTrap = min(largeLeft[i-1], largeRight[i+1])
            if(height[i] > maxRainWaterYouCanTrap):
                rainWaterTrapped.append(0)
                continue
            rainWaterTrapped.append(maxRainWaterYouCanTrap - height[i])
        return sum(rainWaterTrapped)
        """
        :type height: List[int]
        :rtype: int
        """
        

# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

'''
TLDR: Took 2 pointer approach.

Calculate volume for every left and right height.
If one height is less than other, then advance the pointer.
'''
class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        maxVolume = 0
        while(right > left):
            # current volume is minumum height * space between 2 poles.
            currentVolume = min(height[left], height[right]) * (right - left)
            maxVolume = max(maxVolume, currentVolume)
            # if one height is less than other, move that pointer.
            if(height[right] < height[left]):
                right = right - 1
            else:
                left = left + 1
        return maxVolume
        """
        :type height: List[int]
        :rtype: int
        """
        

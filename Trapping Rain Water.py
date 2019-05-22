#Trapping Rain Water
#https://leetcode.com/problems/trapping-rain-water/
class Solution(object):
    def highBarOnLeft(self,heights):
        output = []
        highSoFar = 0
        for height in heights:
            output.append(highSoFar)
            if(height > highSoFar):
                highSoFar = height
        return output

    def highBarOnRight(self, heights):
        output = []
        highSoFar = 0
        for height in reversed(heights):
            output.append(highSoFar)
            if(height > highSoFar):
                highSoFar = height
        output.reverse()
        return output

    def logic(self, heights, left, right):
        i = 1
        unitsOfWater = 0
        while(i < len(heights)-1):
            if(heights[i] < left[i] and heights[i] < right[i]):
                unitsOfWater = unitsOfWater +  (min(right[i], left[i]) - heights[i])
            i = i+1
        return unitsOfWater
            
    def trap(self, height):
        #so the approch goes like this:
        #at each bar calculate the highest bar on left and highest bar on right.
        left = self.highBarOnLeft(height)
        right = self.highBarOnRight(height)
        return self.logic(height, left, right)
        """
        :type height: List[int]
        :rtype: int
        """
#Main
obj = Solution()
print obj.trap([0,1,0,2,1,0,1,3,2,1,2,1])

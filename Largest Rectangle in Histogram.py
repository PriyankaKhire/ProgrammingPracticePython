# Largest Rectangle in Histogram
#https://leetcode.com/problems/largest-rectangle-in-histogram/description/

#with each bar as center ofrectangle how many rectangles around it can we add ?
class Approch1(object):

    def isValid(self, maxHeightIndex, currBarIndex, heights):
        if(heights[currBarIndex] >= heights[maxHeightIndex]):
            return True
        return False

    def addBars(self, currBarIndex, heights):
        height = heights[currBarIndex]
        width = 1
        #add bars from left
        for i in range(currBarIndex-1, -1,-1):
            if(self.isValid(currBarIndex, i, heights)):
                width = width+1
            else:
                #we break because we want contigious
                break
        #add bars from right
        for i in range(currBarIndex+1, len(heights)):
            if(self.isValid(currBarIndex, i, heights)):
                width = width +1
            else:
                #we break because we want contigious
                break
        return width*height
    
    def largestRectangleArea(self, heights):
        maxArea = 0
        for i in range(len(heights)):
            area = self.addBars(i, heights)
            if(area > maxArea):
                maxArea = area
        print maxArea
        """
        :type heights: List[int]
        :rtype: int
        """

#Main
o = Approch1()
o.largestRectangleArea([2,1,5,6,3,4])

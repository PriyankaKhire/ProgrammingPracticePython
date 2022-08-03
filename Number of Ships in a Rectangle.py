# Number of Ships in a Rectangle
# https://leetcode.com/problems/number-of-ships-in-a-rectangle/
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight, bottomLeft):
#        """
#        :type topRight: Point
#		 :type bottomLeft: Point
#        :rtype bool
#        """
#
#class Point(object):
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

class Solution(object):
    def divide(self, sea, topRight, bottomLeft):
        # if invalid rectangle
        if (bottomLeft.x > topRight.x or bottomLeft.y > topRight.y):
            return 0
        # check if this square has ship
        if (not sea.hasShips(topRight, bottomLeft)):
            return 0
        # if the points are the same and we have already checked above that ship is found return 1
        if (topRight.x == bottomLeft.x and topRight.y == bottomLeft.y):
            return 1
        # find mid point 
        midX = (topRight.x+bottomLeft.x)/2
        midY = (topRight.y+bottomLeft.y)/2
        # divide in 4 parts
        topLeftSquare = self.divide(sea, Point(midX, topRight.y), Point(bottomLeft.x, midY+1))
        topRightSqaure = self.divide(sea, topRight, Point(midX+1, midY+1))
        bottomLeftSquare = self.divide(sea, Point(midX, midY), bottomLeft)
        bottomRightSquare = self.divide(sea, Point(topRight.x, midY), Point(midX+1, bottomLeft.y))
        return topLeftSquare + topRightSqaure + bottomLeftSquare + bottomRightSquare
        
        
    def countShips(self, sea, topRight, bottomLeft):
        return self.divide(sea, topRight, bottomLeft)
        """
        :type sea: Sea
        :type topRight: Point
        :type bottomLeft: Point
        :rtype: integer
        """
        

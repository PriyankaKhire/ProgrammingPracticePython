#Triangle
#https://leetcode.com/problems/triangle/

class Solution(object):
    def __init__(self):
        self.tempTriangle = []

    def displayTriangle(self):
        for row in range(len(self.tempTriangle)):
            print self.tempTriangle[row]
        
    def fillTempTriangle(self, triangle):
        self.tempTriangle[0][0] = triangle[0][0]
        for row in range(1, len(triangle)):
            col = 0
            while(col < len(triangle[row])):
                #Add the min of top or prev top value
                #now since its a triangle either the top or top left value can be missing
                top = 99999999999
                topLeft = 99999999999
                if(col < len(triangle[row-1])):
                   top = self.tempTriangle[row-1][col]
                if(col-1 >=0):
                   topLeft = self.tempTriangle[row-1][col-1]
                self.tempTriangle[row][col] = triangle[row][col] + min(top, topLeft)
                col = col+1
        
    def minimumTotal(self, triangle):
        self.tempTriangle = [[0 for col in range(len(triangle))] for row in range(len(triangle))]
        self.fillTempTriangle(triangle)
        self.displayTriangle()
        return min(self.tempTriangle[-1])
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

#Main
obj1 = Solution()
print obj1.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])

print "\n"

obj2 = Solution()
print obj2.minimumTotal([[2],[3,4],[6,5,0],[4,1,8,0]])

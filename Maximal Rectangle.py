#Maximal Rectangle
#https://leetcode.com/problems/maximal-rectangle/description/

class Approch1(object):
    
    def isValid(self, row, col, matrix):
        if(row >=0 and row < len(matrix)):
            if (col >=0 and col < len(matrix[0])):
                if(matrix[row][col] == "1"):
                    return True
        return False
    
    #go in down direction to get height
    def getHeight(self, row, col, matrix):
        height = 0
        while(self.isValid(row, col, matrix)):
            row = row+1
            height = height+1
        return height

    def searchLeft(self, row, col, height, matrix):
        width = 0
        for c in range(col-1, -1, -1):
            for r in range(row, row+height):
                if (matrix[r][c] == "0"):
                    return width
            width = width +1
        return width

    def searchRight(self, row, col, height, matrix):
        width = 0
        for c in range(col+1, len(matrix[0])):
            for r in range(row, row+height):            
                if (matrix[r][c] == "0"):
                    return width
            width = width +1
        return width
        
    #with current bar, we need to find max width this bar can have
    def getWidth(self, height, row, col, matrix):
        width = 1
        #search on left
        width = width + self.searchLeft(row, col, height, matrix)
        #search on right
        width = width + self.searchRight(row, col, height, matrix)
        return width
            
    def maximalRectangle(self, matrix):
        maxArea = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if(matrix[row][col] == "1"):
                    height = self.getHeight(row, col, matrix)
                    width = self.getWidth(height, row, col, matrix)
                    if(maxArea < (width*height)):
                        maxArea = (width*height)
        print maxArea
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

#Main
m = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
m = [
    ["1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","0","0","0"],
    ["0","1","1","1","1","0","0","0"]
]


o = Approch1()
o.maximalRectangle(m)

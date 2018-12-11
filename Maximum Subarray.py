#Maximum Subarray
#https://leetcode.com/problems/maximum-subarray/description/
class Solution(object):
    def __init__(self, array):
        self.array = array
        self.matrix = [[0 for col in range(len(array))] for row in range(len(array))]
        self.largestSum = 0
        self.largestSumRow = None
        self.largestSumCol = None

    def displayMatrix(self):
        for row in range(len(self.array)):
            print self.matrix[row]

    def fillMatrix(self):
        for row in range(len(self.array)):
            for col in range(row, len(self.array)):
                if(row == col):
                    self.matrix[row][col] = self.array[row]
                else:
                    self.matrix[row][col] = self.matrix[row][col-1] + self.array[col]
                    #find the largest sum
                    if(self.largestSum < self.matrix[row][col]):
                        self.largestSum = self.matrix[row][col]
                        self.largestSumRow = row
                        self.largestSumCol = col

    def logic(self):
        self.fillMatrix()
        self.displayMatrix()
        print "The largest sum subarray lies between ", self.array[self.largestSumRow:self.largestSumCol+1]
        print "The largest sum is ", self.largestSum

#Main
obj = Solution([-2,1,-3,4,-1,2,1,-5,4])
obj.logic()

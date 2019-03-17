#Range Sum Query 2D - Immutable
#https://leetcode.com/problems/range-sum-query-2d-immutable/
class NumMatrix(object):

    def __init__(self, matrix):
        self.matrix = matrix
        self.solutionMatrix = [[0 for col in range(len(matrix)+1)] for row in range(len(matrix)+1)]
        self.fillMatrix()
        print self.solutionMatrix
        
    def fillMatrix(self):
        for row in range(1, len(self.matrix)+1):
            for col in range(1, len(self.matrix)+1):
                #up+left+current-diagonal (coz diagonal is added twice)
                #check if given input matrix is 1d or 2d
                if(isinstance(self.matrix[0], list)):
                    self.solutionMatrix[row][col] = (self.solutionMatrix[row-1][col]+self.solutionMatrix[row][col-1]+self.matrix[row-1][col-1])-self.solutionMatrix[row-1][col-1]
                else:
                    self.solutionMatrix[row][col] = (self.solutionMatrix[row-1][col]+self.solutionMatrix[row][col-1]+self.matrix[row-1])-self.solutionMatrix[row-1][col-1]
                

    def sumRegion(self, row1, col1, row2, col2):
        #current rectangle is formed by r1, c1 as top left diagonal and r2, c2 as bottom right diagonal
        #in our soluiton matrix the bottom diagonal represents sum from 0, 0 to bottom right diagonal
        #let us take an example matrix where o represents some value
        #  0 1 2 3 4
        #0 o o o o o
        #1 o O O O o
        #2 o O O O o
        #3 o O O O o
        #now we wanna find sum from 1,1 to 3,3  represented by O
        #we create a soluiton matrix
        #  0 1 2 3 4 5
        #0 o o o o o o
        #1 o o o o o o
        #2 o o o o o o
        #3 o o o o o o
        #4 o o o o o o
        #we have added exra row and col. now cel 1,1 represents sum in the original matrix from 0,0 to 1,1
        # so cell 4,4 would represent sum of rectangle from 0,0 to 3,3
        #but in our original query we only wanna find sum from 1,1 and dont want row 0 and col 0 added to it
        #  0 1 2 3 4 5
        #0 o o o o o o
        #1 X x x x x o
        #2 x O O O o 
        #3 x O O O o 
        #4 x O O O o
        #so to find the sum we take the diagonal 4,4 subctract 1,4 and 4,0 from it and see the big X
        #that gets subctracted twice because 1,4 is addition from 0,0 to 0,3 in origonal matrix
        #and 4,0 is 0,0 to 3,0 so we add the big X at 1,1
        #thus the formula becomes: solMatrix[r2][c2] - top - left + diagonal
        #since the rows and cols here are for original matrix and not our solution matrix we need to add 1 to all of them
        row1 = row1+1
        row2 = row2+1
        col1 = col1+1
        col2 = col2+1
        return self.solutionMatrix[row2][col2] - self.solutionMatrix[row1-1][col2] - self.solutionMatrix[row2][col1-1] + self.solutionMatrix[row1-1][col1-1]
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
#Main
print "for matrix 1"
matrix1 = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
    ]
obj = NumMatrix(matrix1)
print obj.sumRegion(2,1,4,3)
print obj.sumRegion(1,1,2,2)
print obj.sumRegion(1,2,2,4)
print "for matrix 2"
matrix2 = [
    [2,0,-3,4],
    [6,3,2,-1],
    [5,4,7,3],
    [2,-6,8,1]
    ]
obj2 = NumMatrix(matrix2)
print obj2.sumRegion(1,1,3,2)
print obj2.sumRegion(2,3,3,3)
print obj2.sumRegion(3,3,3,3)
#print "for matrix 3"
#matrix3 = [-4,-5]
#obj3 = NumMatrix(matrix3)
#print obj3.sumRegion(0,0,0,0)
#print obj3.sumRegion(0,0,0,1)
#print obj3.sumRegion(0,1,0,1)

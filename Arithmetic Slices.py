#Arithmetic Slices
#https://leetcode.com/problems/arithmetic-slices/

class DP1(object):
    def __init__(self):
        self.matrix = None

    def displayMatrix(self):
        for row in range(len(self.matrix)):
            print self.matrix[row]

    def fillMatrix(self, A):
        row = 0
        col = 0
        startC = 0
        length = 1
        numSlices = 0
        while(startC < len(A)):
            if(length < 3):
                self.matrix[row][col] = A[row] - A[col]
            else:
                if(self.matrix[row][col-1] == self.matrix[row+1][col] and self.matrix[row][col-1] != -999):
                    self.matrix[row][col] = True
                    numSlices = numSlices+1
                else:
                    self.matrix[row][col] = -999
            row = row+1
            col = col+1
            if(col == len(A)):
                row = 0
                startC = startC+1
                col = startC
                length = length+1
        return numSlices
        
    def numberOfArithmeticSlices(self, A):
        self.matrix = [[0 for col in range(len(A))] for row in range(len(A))]
        print self.fillMatrix(A)
        self.displayMatrix()
        """
        :type A: List[int]
        :rtype: int
        """

#Main
obj1 = DP1()
obj1.numberOfArithmeticSlices([1,2,3,4,5])

obj2 = DP1()
obj2.numberOfArithmeticSlices([1,2,3,9,4,5])

obj3 = DP1()
obj3.numberOfArithmeticSlices([1,1,1,1])

obj4 = DP1()
obj4.numberOfArithmeticSlices([18, -36, 18])

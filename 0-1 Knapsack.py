#0-1 Knapsack Problem
#https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

class Solution(object):
    def __init__(self, values, weights, maxWt):
        self.val = values
        self.wt = weights
        self.maxWt = maxWt
        self.matrix = [[0 for col in range(maxWt+1)] for row in range(len(self.val)+1)]

    def displayMatrix(self):
        for row in range(len(self.matrix)):
            print self.matrix[row]

    def fillMatrix(self):
        for row in range(1, len(self.matrix)):
            for col in range(1, len(self.matrix[0])):
                #1) if wt is > given weight : copy value from top
                if(self.wt[row-1] > col):
                    self.matrix[row][col] = self.matrix[row-1][col]
                else:
                    #2) if wt <= given weight : max(matrix[given wt - wt]+val[wt], top)
                    self.matrix[row][col] = max(self.matrix[row-1][col-self.wt[row-1]]+self.val[row-1], self.matrix[row-1][col])

    def logic(self):
        print "The max allotted weight is ", self.maxWt
        self.fillMatrix()
        self.displayMatrix()
        print "The max item value that can be added in knapsack is ", self.matrix[-1][-1]

#Main
obj = Solution([1,4,5,7],[1,3,4,5],7)
obj.logic()

obj = Solution([60,100,120],[10,20,30],50)
obj.logic()

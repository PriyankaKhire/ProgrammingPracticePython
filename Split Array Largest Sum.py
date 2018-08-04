#Split Array Largest Sum
#
#Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.
#
#Note:
#If n is the length of array, assume the following constraints are satisfied:
#
#1 ≤ n ≤ 1000
#1 ≤ m ≤ min(50, n)
#Examples:
#
#Input:
#nums = [7,2,5,10,8]
#m = 2
#
#Output:
#18
#
#Explanation:
#There are four ways to split nums into two subarrays.
#The best way is to split it into [7,2,5] and [10,8],
#where the largest sum among the two subarrays is only 18.
class Approch1(object):
    def __init__(self, array, m):
        self.array = array
        self.m = m
        self.matrix = [[0 for col in range(len(array))] for row in range(len(array))]
        self.smallMaxSum = None
        
    def createMatrix(self):
        for row in range(len(self.array)):
            for col in range(row, len(self.array)):
                if row == col:
                    self.matrix[row][col] = self.array[row]
                else:
                    self.matrix[row][col] = self.matrix[row][col-1] + self.array[col]

    def iterateMatrix(self, row, currSet, currM, remainingNumbers):
        if(currM == 0 and remainingNumbers != 0):
            return
        if(currM == 0 and remainingNumbers == 0):
            print currSet
            if (self.smallMaxSum == None or self.smallMaxSum > max(currSet)):
                self.smallMaxSum = max(currSet)
            return
        #Add current number to current set
        numbersAdded = 0
        for c in range(row, len(self.array)):
            numbersAdded = numbersAdded + 1
            currSet.append(self.matrix[row][c])
            self.iterateMatrix(c+1, currSet, currM-1, remainingNumbers-numbersAdded)
            currSet.pop()
                
        
    def solution(self):
        if(self.m > len(self.array)):
            return max(self.array)
        self.createMatrix()
        print self.matrix
        self.iterateMatrix(0, [], self.m, len(self.array))
        print self.smallMaxSum
        
        

#Main
o = Approch1([8,2,5,6,1,4], 4)
o.solution()

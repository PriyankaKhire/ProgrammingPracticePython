#Perfect Squares
#https://leetcode.com/problems/perfect-squares/
import math

class Solution(object):
    def __init__(self):
        self.array = []
        self.squares = []

    #fill the array with squares that are less than n
    #for example if n = 12, the squares that are less than 12 are 1,4,9
    def fillSqaures(self, n):
        for i in range(1, n):
            if(i**2 > n):
                return 
            self.squares.append(i**2)

    def findMin(self, num, squarePointer):
        answer = num
        for i in range(squarePointer, -1, -1):
            remainder = num - self.squares[i]
            if(self.array[remainder]+1 < answer):
                answer = self.array[remainder]+1
        return answer

    def fillArray(self, n):
        squarePointer = 0
        for i in range(1, n+1):
            #Advance square pointer
            if(squarePointer+1 < len(self.squares) and self.squares[squarePointer+1] == i):
                self.array[i] = 1
                squarePointer = squarePointer+1
                continue
            self.array[i] = self.findMin(i, squarePointer)
        
    def numSquares(self, n):
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        #See if the number is already a perfect square
        if(math.sqrt(n).is_integer()):
            return 1
        self.array = [0 for i in range(n+1)]
        self.fillSqaures(n)
        self.fillArray(n)
        return self.array[-1]
        """
        :type n: int
        :rtype: int
        """

#Main
obj = Solution()
print obj.numSquares(13)

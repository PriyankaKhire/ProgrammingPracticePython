#Edit Distance
# https://leetcode.com/problems/edit-distance/description/
class Solution(object):
    def __init__(self):
        self.matrix = []

    def displayMatrix(self):
        for row in range(len(self.matrix)):
            print self.matrix[row]

    def fillMatrix(self, word1, word2):
        #fill initial 0th row and col
        for col in range(len(word1)+1):
            self.matrix[0][col] = col
        for row in range(len(word2)+1):
            self.matrix[row][0] = row
        for row in range(1, len(word2)+1):
            for col in range(1, len(word1)+1):
                #1) when 2 chars are equal: copy diagonal top left square value
                if(word1[col-1] == word2[row-1]):
                    self.matrix[row][col] = self.matrix[row-1][col-1]
                else:
                    #2) when not equal: min(top left, left, top) +1
                    self.matrix[row][col] = min(self.matrix[row-1][col-1], self.matrix[row][col-1], self.matrix[row-1][col])+1
                
        
    def minDistance(self, word1, word2):
        self.matrix = [[0 for col in range(len(word1)+1)] for row in range(len(word2)+1)]
        self.fillMatrix(word1, word2)
        self.displayMatrix()
        print "The min distance reqired to convert "+word1+" to "+word2+" is ", self.matrix[-1][-1]
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

#Main
obj1 = Solution()
obj1.minDistance("horse", "ros")

obj2 = Solution()
obj2.minDistance("intention", "execution")

obj3 = Solution()
obj3.minDistance("a", "ab")

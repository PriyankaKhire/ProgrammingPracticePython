#Longest Common Subsequence
#https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

class Solution(object):
    def __init__(self, sequence1, sequence2):
        self.s1 = sequence1
        self.s2 = sequence2
        self.matrix = [[0 for col in range(len(self.s1)+1)] for row in range(len(self.s2)+1)]

    def displayMatrix(self):
        for row in range(len(self.matrix)):
            print self.matrix[row]

    def formMatrix(self):
        for row in range(1, len(self.matrix)):
            #$$we start from 1 instead of 0
            for col in range(1, len(self.matrix[0])):
                #1) if the letters are same then add one to diagonal box
                #we subctract 1 from row and column because we start from 1 here $$
                if(self.s1[col-1] == self.s2[row-1]):
                    self.matrix[row][col] = 1+(self.matrix[row-1][col-1])
                else:
                    #2)if the letters are not equal: we take max of one row up or one col before.
                    self.matrix[row][col] = max(self.matrix[row-1][col], self.matrix[row][col-1])
                    
    def logic(self):
        print "For strings "+self.s1+" and "+self.s2
        self.formMatrix()
        print "The dynamic programming matrix is "
        self.displayMatrix()
        print "The longest Common Subsequence is ",self.matrix[-1][-1]

#Main
obj = Solution("ABCDAF", "ACBCF")
obj.logic()

obj = Solution("AGGTAB", "GXTXAYB")
obj.logic()

obj = Solution("ABCDGH", "AEDFHR")
obj.logic()

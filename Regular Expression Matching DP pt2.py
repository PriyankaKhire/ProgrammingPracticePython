#Regular Expression Matching
#https://leetcode.com/problems/regular-expression-matching/
class Solution(object):
    def __init__(self):
        self.matrix = None

    def displayMatrix(self):
        for row in range(len(self.matrix)):
            print self.matrix[row]
        print "\n"

    def fillMatrix(self, s, p):
        self.matrix[0][0] = True
        #Fill first row
        for col in range(1, len(p)+1):
            if(p[col-1] == '*'):
                #for zero occourances look at 2 spaces behind
                self.matrix[0][col] = self.matrix[0][col-2]
        #Fill rest of the rows
        for row in range(1, len(s)+1):
            for col in range(1, len(p)+1):
                if(p[col-1] == '.'):
                    self.matrix[row][col] = self.matrix[row-1][col-1]
                elif(p[col-1] == '*'):
                    #look at the previous char if it matches then copy value from top
                    #for zero occourances look at 2 spaces behind
                    self.matrix[row][col] = max(self.matrix[row-1][col], self.matrix[row][col-2])                                        
                elif(p[col-1] == s[row-1]):
                    self.matrix[row][col] = self.matrix[row-1][col-1]
        
    def isMatch(self, s, p):
        self.matrix = [[False for col in range(len(p)+1)] for row in range(len(s)+1)]
        self.fillMatrix(s, p)
        self.displayMatrix()
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
#Main
obj = Solution()
obj.isMatch("mississippi", "mis*is*p*.")
"mississippi"
"mis*is*p*."

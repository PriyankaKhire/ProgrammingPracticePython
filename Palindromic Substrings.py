#Palindromic Substrings
#https://leetcode.com/problems/palindromic-substrings/
class DP(object):
    def __init__(self):
        self.matrix = None

    def fillMatrix(self, s):
        #diagonal matrix traversal
        row = 0
        col = 0
        startC = 0
        while(row < len(s) and startC < len(s)):
            if (row == col):
                self.matrix[row][col] = 1
            else:
                if(s[row] == s[col]):
                    #if length is 2 then its a palindrome
                    # for length greater than 2, check if inner palindrome or not
                    if(row == col-1 or self.matrix[row+1][col-1] == 1):
                        self.matrix[row][col] = 1
            row = row+1
            col = col+1
            if(col == len(s)):
                row = 0
                startC = startC+1
                col = startC
                
    def logic(self, s):
        self.fillMatrix(s)
        #count the number of one's in matrix and thats your answer
        output = 0
        for row in range(len(s)):
            for col in range(len(s)):
                if(self.matrix[row][col] == 1):
                    output = output + 1
        return output
    
    def countSubstrings(self, s):
        self.matrix = [[0 for col in range(len(s))] for row in range(len(s))]
        print self.logic(s)
        """
        :type s: str
        :rtype: int
        """

#Main
obj1 = DP()
obj1.countSubstrings("abc")

obj2 = DP()
obj2.countSubstrings("aaa")

#Regular Expression Matching
#https://leetcode.com/problems/regular-expression-matching/description/
class Solution(object):
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern
        self.matrix = [[0 for col in range(len(pattern)+1)] for row in range(len(string)+1)]

    def displayMatrix(self):
        for row in range(len(self.string)+1):
            print self.matrix[row]
            
    def fillMatrix(self):
        for row in range(len(self.string)+1):
            for col in range(len(self.pattern)+1):

    def logic(self):
        self.fillMatrix()
        self.displayMatrix()


#Main
obj = Solution("", "")
obj.logic()

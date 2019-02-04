#Distinct Subsequences
#https://leetcode.com/problems/distinct-subsequences/

class DP(object):
    def __init__(self):
        self.matrix = None

    def displayMatrix(self):
        for row in range(len(self.matrix)):
            print self.matrix[row]

    def fillMatrix(self, s, t):
        #fill first row
        for col in range(len(s)+1):
            self.matrix[0][col] = 1
        #fill first col
        #this for loop is unnecessary but you need to get idea.
        #for row in range(len(t)+1):
            #self.matrix[row][0] = 0
        for row in range(1, len(t)+1):
            for col in range(1, len(s)+1):
                if(row > col):
                    continue
                if(t[row-1] != s[col-1]):
                    #borrow from side
                    self.matrix[row][col] = self.matrix[row][col-1]
                else:
                    #We add up side and diagonal top left
                    # why side, it tells the previous instances of the same char
                    #like for example in s = bagg and t = bag, char g occours 2 times in s
                    # this is dipected in left cell of matrix of a row, coz row represents a char from t
                    # why diagonal top left, it represents string so far before this char in t
                    # so if so far the string doesnt match it would be 0 and if the char has not been encounterd before it would also be 0
                    # but now you suddenly see that char then it shouldnt be 1 coz previous string doesnt match
                    # for example s = rzzb t = rabb, no matter how many characters you delete from s you can never make it into t
                    self.matrix[row][col] = self.matrix[row][col-1]+self.matrix[row-1][col-1]
                    
        
    def numDistinct(self, s, t):
        self.matrix = [[0 for col in range(len(s)+1)] for row in range(len(t)+1)]
        self.fillMatrix(s, t)
        print "for s = ", s, " and t = ", t
        self.displayMatrix()
        print "\n"
        """
        :type s: str
        :type t: str
        :rtype: int
        """
#Main
obj1 = DP()
obj1.numDistinct("rabbbit", "rabbit")

obj2 = DP()
obj2.numDistinct("babgbag", "bag")

#this example shows occourance of character as g occours 2ce.
#note the last row in matrix.
obj3 = DP()
obj3.numDistinct("baggbag", "bag")

#this example shows the importance of matching the previous string so the top diagonal left
obj4 = DP()
obj4.numDistinct("rzzb", "rabb")

obj5 = DP()
obj5.numDistinct("abcde", "ace")

#  Compare RLE Strings
class Solution(object):

    def getNumber(self, s):
        num = ""
        while not(s[0].isalpha()):
            num = num + s[0]
            # pop first character from string
            s = s[1:]
        return int(num), s
        
    def compare(self, s, t):
        while(s!="" and t!=""):
            print "string s is",s,"string t is",t
            sNum, s = self.getNumber(s)
            while(sNum == 0 and s!=""):
                print "Since sNum is zero we drop the character after the number, the string s is",s
                s = s[1:]
                if s!="":
                    sNum, s = self.getNumber(s)
            print "The number ahead of s is",sNum,"The string s now is",s
            tNum, t = self.getNumber(t)
            while(tNum == 0 and t!=""):
                print "Since tNum is zero we drop the character after the number, the string t is",t
                t = t[1:]
                if t!="":
                    tNum, t = self.getNumber(t)
            print "The number ahead of t is",tNum,"The string t now is",t
            if(s=="" and t==""):
                print "Since the strings became null, they are equal"
                return True
            if(s[0] == t[0]):
                if(sNum < tNum):
                    tNum = tNum-sNum
                    sNum = 0                 
                elif(sNum > tNum):
                    sNum = sNum - tNum
                    tNum = 0 
                elif(sNum == tNum):
                    sNum = 0
                    tNum = 0
                print "After subctraction sNum is",sNum,"and tNum is",tNum
                s = str(sNum)+s
                t = str(tNum)+t
                print "After modification the string s is",s,"the string t is",t
            else:
                return False

    # this function uses O(n) space
    def boardRowsLeftToRight(self, s, width):
        board = []
        row = []
        w = width
        while(s!=""):
            print "The board is",board,"row is","current width is",w
            if(w == 0):
                board.append(row)
                row = []
                w = width
            sNum, s = self.getNumber(s)
            print "Number in front of s is",sNum,"the string s is",s
            while(sNum == 0 and s!=""):
                print "The number in front of s is zero so we remove it"
                s = s[1:]
                if(s!=""):
                    sNum, s = self.getNumber(s)
            print "String after removing leadign zeros is",s,"and the current number in front of it is",sNum
            if(s==""):
                print "The string has become empty so we return the board"
                return board
            if(sNum < w):
                row.append(str(sNum)+s[0])
                s = s[1:]
                w = w-sNum
            elif(sNum > w):
                row.append(str(w)+s[0])
                sNum = sNum-w
                s = str(sNum)+s
                w = 0
            elif(sNum == w):
                row.append(str(sNum)+s[0])
                sNum = 0
                w = 0
                s = str(sNum)+s
            print "The current row is ",row

    def boardRowsRightToLeft(self, s, width):
        board = self.boardRowsLeftToRight(s, width)
        print "The board row from left to right is"
        print "Reversed board is"
        for row in board:
            row.reverse()
        print board
        print "Board in string form is"
        string = ""
        for row in board:
            string = string + ''.join(row)
        print string
            
            
# Main
s = "3a1b3c"
t = "2a1a1b2c1d"
obj = Solution()
#print obj.compare(s,t)

s = "3a1b"
t = "2a1a1b"
obj = Solution()
#print obj.compare(s,t)

s = "3a1b3c3d2a"
width = 4
obj.boardRowsRightToLeft(s, width)

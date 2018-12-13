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

    def fillNullRow(self):
        #Null column is going to be false for all row
        #because when pattern is null, no matter what the string is, it's going to be false.
        #when col is Null and row is null its true.
        self.matrix[0][0] = 1
        #fill null row
        for col in range(1,len(self.pattern)+1):
            if(self.pattern[col-1] == '.' and col ==1):
                self.matrix[0][col] = 1
            elif(self.pattern[col-1] == '*'):
                # for cases where p = ".*" or "*"
                if(col == 1 or (col > 1 and self.pattern[col-2] == '.')):
                    self.matrix[0][col] = 1
            
    def fillMatrix(self):
        self.fillNullRow()
        #we start from 1 because the null row and col are filled.
        # and null is first row and col.
        for row in range(1,len(self.string)+1):
            for col in range(1,len(self.pattern)+1):
                print "row ", row, " col ", col
                print "string ", self.string[row-1], " pattern ", self.pattern[col-1]
                #1) if pattern and string are same:
                # chek the top left diagonal square, if its true then matrix[row][col] = true
                if(self.pattern[col-1] == self.string[row-1]):
                    print "top left square is true "
                    self.matrix[row][col] = self.matrix[row-1][col-1]
                else:
                    #2) if pattern and string are not the same:
                    #2a) if pattern is alphabet
                    if(self.pattern[col-1].isalpha()):
                        print "pattern is a letter "
                        #if that letter is not exual to string letter then false
                        if(self.pattern[col-1] != self.string[row-1]):
                            print "and that letter is not equal to string"
                            self.matrix[row][col] = 0
                    else:
                        print "pattern is a special char"
                        #if pattern is *
                        if(self.pattern[col-1] == '*'):
                            print "pattern is *"
                            print "previous letter to the pattern is ", self.pattern[col-2]
                            #if previous pattern character is a letter and that letter is == to string letter
                            if(self.pattern[col-2] == self.string[row-1]):
                                if(self.matrix[row][col-1] == 1):
                                    self.matrix[row][col] = 1
                                else:
                                    print "this is equal to current string letter"
                                    self.matrix[row][col] = self.matrix[row-1][col-1]
                            elif(self.pattern[col-2] != '.' and (self.pattern[col-2] != self.string[row-1] or self.pattern[col-2] == '*')):
                                print "this is not equal to string letter"
                                self.matrix[row][col] = self.matrix[row][col-2]
                            elif(self.pattern[col-2] == '.'):
                                print "its a dot"
                                self.matrix[row][col] = 1
                        #if pattern is .                       
                        elif(self.pattern[col-1] == '.'):
                            print "current pattern char is a dot"
                            #that means it's the first character in pattern
                            if col == 1:
                                print "dot is in first col"
                                self.matrix[row][col] = 1
                            else:
                                print "dot is irrelevant coz we copy values from top left"
                                self.matrix[row][col] = self.matrix[row-1][col-1]

    def logic(self):
        self.fillMatrix()
        self.displayMatrix()


#Main
#obj1 = Solution("xaabyc", "xa*b.c")
#obj1.logic()

#obj2 = Solution("ab", ".*")
#obj2.logic()

#obj3 = Solution("aa", "a")
#obj3.logic()

#obj4 = Solution("aa", "a*")
#obj4.logic()

obj5 = Solution("aab", "c*a*b")
obj5.logic()

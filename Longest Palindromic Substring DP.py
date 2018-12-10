#Longest Palindromic Substring
#https://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

class Solution(object):
    def __init__(self, string):
        self.string = string
        self.matrix = [[0 for col in range(len(string))] for row in range(len(string))]
        self.longestPalindromeLength = 0
        self.longestPalindromeRow = None
        self.longestPalindromeCol = None

    def numberOfCellsBetweenRowCol(self, row, col):
        if(row > col):
            return row - col - 1
        return col - row - 1

    def displayMatrix(self):
        for row in range(len(self.string)):
            print self.matrix[row]

    def fillMatrix(self):
        #we fill the matrix diagonally
        row = 0
        col = 0
        colStart = 0
        while(row <= len(self.string) and colStart < len(self.string)):
            #if row == col for initial big diagonal
            if(row == col):
                self.matrix[row][col] = 1
            else:
                #1) if 2 letters are not same then:
                # max(left or bottom)
                #print row, col
                if(self.string[row] != self.string[col]):
                    self.matrix[row][col] = max(self.matrix[row][col-1], self.matrix[row+1][col])
                    #print "The max of ", row, col-1, " and ", row+1, col, " is ", max(self.matrix[row][col-1], self.matrix[row+1][col])
                else:
                    #2) if 2 letters are same then:
                    #check the diagonal bottom, is the number there == number of spaces between row and col
                    #if yes then add 2 to that number and fill the cell
                    #if not  then copy max of left or bottom.
                    numSpaces = self.numberOfCellsBetweenRowCol(row, col)
                    #print "the number of spaces between ", row, col, " is ", numSpaces
                    #print "and the diagonal bottom ", row+1, col-1, " is ", self.matrix[row+1][col-1]
                    if(numSpaces == self.matrix[row+1][col-1]):
                        self.matrix[row][col] = 2+self.matrix[row+1][col-1]
                        #print "so we fill ", self.matrix[row][col] 
                    else:
                        #print "else The max of ", row, col-1, " and ", row+1, col, " is ", max(self.matrix[row][col-1], self.matrix[row+1][col])
                        self.matrix[row][col] = max(self.matrix[row][col-1], self.matrix[row+1][col])
                        #print "so we fill ", self.matrix[row][col]
                #record longest palindrome row and col
                if(self.longestPalindromeLength < self.matrix[row][col]):
                    self.longestPalindromeLength = self.matrix[row][col]
                    self.longestPalindromeRow = row
                    self.longestPalindromeCol = col
            row = row+1
            col = col+1
            if(row == len(self.string) or col == len(self.string)):
                row = 0
                colStart = colStart+1
                col = colStart

    def logic(self):
        print "For string ", self.string
        self.fillMatrix()
        self.displayMatrix()
        print "The longest palindromic substring is of length ", self.matrix[0][-1]
        print "The longest palindromic substring is ", self.string[self.longestPalindromeRow:self.longestPalindromeCol+1]
        

#Main
obj1 = Solution("abananapa")
obj1.logic()

obj2 = Solution("forgeeksskeegfor")
obj2.logic()

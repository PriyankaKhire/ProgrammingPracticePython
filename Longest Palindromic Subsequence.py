#Longest Palindromic Subsequence
#https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/

class Solution(object):
    def __init__(self, string):
        self.string = string
        self.matrix = [[0 for col in range(len(string))] for row in range(len(string))]

    def displayMatrix(self):
        for row in range(len(self.string)):
            print self.matrix[row]

    def fillMatrix(self):
        #We fill the matrix diagonally
        row = 0
        col = 0
        colStart = 0
        #The conditions in while loop are to fill diagonally.
        while(row <= len(self.matrix) and col <= len(self.matrix[0]) and colStart < len(self.matrix[0])):
            #Fill the main longest diagonal
            if(row == col):
                self.matrix[row][col] = 1
            else:
                #1)if 2 letters are same then:
                # max(2+diagonal bottom, left, bottom)
                #the logic to add 2 + diagonal bottom is:
                # when we find 2 letters same, it adds 2 to the length of the palindrome
                # and then we see if there is a palindrome between those 2 letters, that is found by adding diagonal bottom
                # then we see if the palindrome is longer by omitting first letter or last letter thats why left and bottom are checked in max
                if(self.string[row] == self.string[col]):
                    self.matrix[row][col] = max((2+self.matrix[row+1][col-1]), self.matrix[row][col-1], self.matrix[row+1][col])
                else:
                    #2) if 2 letters are not the same:
                    # max(left, bottom)
                    # the logic here is we see if the palindrome is longer by omitting first or last letter
                    # thats why left and bottom.
                    self.matrix[row][col] = max(self.matrix[row][col-1], self.matrix[row+1][col])
            row = row+1
            col = col+1
            if(row == len(self.matrix) or col == len(self.matrix[0])):
                row = 0
                colStart = colStart+1
                col = colStart

    def logic(self):
        print "For string "+self.string+" the matrix is "
        self.fillMatrix()
        self.displayMatrix()
        print "The longest palindromic subsequence is ", self.matrix[0][-1]
        
                

#Main
obj1 = Solution("BBABCBCAB")
obj1.logic()

obj2 = Solution("GEEKSFORGEEKS")
obj2.logic()

obj3 = Solution("AGBDBA")
obj3.logic()

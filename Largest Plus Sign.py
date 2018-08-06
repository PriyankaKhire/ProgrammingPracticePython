#Largest Plus Sign
#Difficulty:Medium
#
#In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.
#
#An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.
#
#Examples of Axis-Aligned Plus Signs of Order k:
#
#Order 1:
#000
#010
#000
#
#Order 2:
#00000
#00100
#01110
#00100
#00000
#
#Order 3:
#0000000
#0001000
#0001000
#0111110
#0001000
#0001000
#0000000
#Example 1:
#
#Input: N = 5, mines = [[4, 2]]
#Output: 2
#Explanation:
#11111
#11111
#11111
#11111
#11011
#In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
#Example 2:
#
#Input: N = 2, mines = []
#Output: 1
#Explanation:
#There is no plus sign of order 2, but there is of order 1.
#Example 3:
#
#Input: N = 1, mines = [[0, 0]]
#Output: 0
#Explanation:
#There is no plus sign, so return 0.
#Note:
#
#N will be an integer in the range [1, 500].
#mines will have length at most 5000.
#mines[i] will be length 2 and consist of integers in the range [0, N-1].
#(Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)
class qObject(object):
    def __init__(self, row, col, direction):
        self.row = row
        self.col = col
        self.dir = direction
        self.degr

class Approch1(object):
    def __init__(self, N, mines):
        self.n = N
        self.mines = mines
        self.matrix = []
        self.directions = ["up", "down", "left", "right"]
    
    def constructN(self):
        self.matrix = [[1 for col in range((self.n))] for row in range((self.n))]
        for mine in self.mines:
            r = mine[0]
            c = mine[1]
            self.matrix[r][c] =0
        print self.matrix

    def newRowCol(self, row, col, direction):
        if(direction == "up"):
            row = row-1
        elif(direction == "down"):
            row = row+1
        elif(direction == "left"):
            col = col-1
        elif(direction == "right"):
            col = col+1
        return (row, col)

    def isValid(self, row, col):
        if(self.matrix[row][col] == 1):
            if(row >= 0 and row < self.n):
                if(col >=0 and col < self.n):
                    return True
        return False

    #by default the degree of single 1 is 1 we need to check if it can be more than one
    def bfs(self, row, col):
        q = []
        for direction in self.directions:
            new_r, new_c = self.newRowCol(row, col, direction)
            if not(isValid(new_r, new_c)):
                return 1
            o = qObject(new_r, new_c, direction)
            q.append(o)
        degree = 2
        while(q):
            top = q.pop(0)
            new_r, new_c = self.newRowCol(top.row, top.col, top.direction)
            if not(isValid(new_r, new_c)):
                return degree
            
        
        
    def solution(self):
        #generally if there are no mines then the axis-aligned plus sign of 1s would be
        #of order N-1 but if N = 1 then its 1
        if(self.n == 1):
            if not self.mines:
                return 1
            else:
                return 0
        for row in range(self.n):
            for col in range(self.n):
                if (self.matrix[row][col] == 1):
                    self.bfs(row, col)
        


#Main
o = Approch1(5, [[4,2]])
o.constructN()

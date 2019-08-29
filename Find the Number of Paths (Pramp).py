# -*- coding: cp1252 -*-
# Find the Number of Paths
# https://medium.com/@vickdayaram/find-the-number-of-paths-d7d9cfccba08
'''
You’re testing a new driverless car that is located at the Southwest (bottom-left) corner
of an n×n grid. The car is supposed to get to the opposite, Northeast (top-right), corner
of the grid. Given n, the size of the grid's axes, write a function numOfPathsToDest that
returns the number of the possible paths the driverless car can take.

Matrix

5################/
                             /
4############/
                     /
3########/
              /
2####/
       /
1  /
0    1    2    3    4    5

So where ever there is # you cannot go there.

For convenience, let's represent every square in the grid as a pair (i,j).
The first coordinate in the pair denotes the east-to-west axis, and the second
coordinate denotes the south-to-north axis. The initial state of the car is (0,0),
and the destination is (n-1,n-1).

The car must abide by the following two rules:
it cannot cross the diagonal border. In other words, in every step the position (i,j)
needs to maintain i >= j.(There is an error in problem here, it should be i<=j)
See the illustration above for n = 5. In every step,
it may go one square North (up), or one square East (right), but not both.
E.g. if the car is at (3,1), it may go to (3,2) or (4,1).

Example:
input: n = 4 (so start is 0, 0 and destination is 3,3)
output: 5
since there are 5 possibilities:
EEENNN, EENENN, ENEENN, ENENEN, EENNEN
'''
class Backtracking(object):
    
    def isValid(self, row, col, n):
        if(row >= 0 and row < n):
            if(col >= 0 and col < n):
                if(row <= col):
                    return True
        return False
    
    def logic(self, row, col, n, path, totalPaths):
        if(row == n-1 and col == n-1):
            print path
            totalPaths[0] = totalPaths[0]+1
            return
        # go east
        if(self.isValid(row, col+1, n)):
            self.logic(row, col+1, n, path+"E", totalPaths)
        # go north
        if(self.isValid(row+1, col, n)):
            self.logic(row+1, col, n, path+"N", totalPaths)
        
    def getNumberOfPaths(self, n):
        totalPaths = [0]
        self.logic(0, 0, n, "", totalPaths)
        print "Total paths taken for n =",n,"are: ", totalPaths[0]

# Main
obj = Backtracking()
obj.getNumberOfPaths(0)
obj.getNumberOfPaths(1)
obj.getNumberOfPaths(2)
obj.getNumberOfPaths(3)
obj.getNumberOfPaths(4)
obj.getNumberOfPaths(5)
obj.getNumberOfPaths(6)








        

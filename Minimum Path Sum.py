#Minimum Path Sum
#https://leetcode.com/problems/minimum-path-sum/

class Backtracking(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def isValid(self, row, col):
        if(row >= 0 and row < len(self.matrix)):
            if(col >=0 and col < len(self.matrix)):
                return True
        return False

    def recurrse(self, output, row, col):
        if(row == len(self.matrix)-1 and col == len(self.matrix)-1):
            print output, sum(output)
            return
        #Move right
        if(self.isValid(row, col+1)):
            output.append(self.matrix[row][col+1])
            self.recurrse(output, row, col+1)
            output.pop()
        #move down
        if(self.isValid(row+1, col)):
            output.append(self.matrix[row+1][col])
            self.recurrse(output, row+1, col)
            output.pop()

    def logic(self):
        self.recurrse([self.matrix[0][0]], 0, 0)

class DP(object):

    def isValid(self, row, col, grid):
        if(row >=0 and row < len(grid)):
            if(col >= 0 and col < len(grid[0])):
                return True
        return False
    
    def fillMatrix(self, grid):
        for row in range(len(grid)-1, -1, -1):
            for col in range(len(grid[0])-1, -1, -1):
                #for the last cell grid[-1][-1]
                if not(self.isValid(row+1, col, grid) or self.isValid(row, col+1, grid)):
                    continue
                #for rest of them
                down = 99999
                right = 99999
                if(self.isValid(row+1, col, grid)):
                    down = grid[row+1][col]
                if(self.isValid(row, col+1, grid)):
                    right = grid[row][col+1]
                grid[row][col] = grid[row][col] + min(down, right)
                
    def minPathSum(self, grid):
        self.fillMatrix(grid)
        print grid[0][0]
        """
        :type grid: List[List[int]]
        :rtype: int
        """

#Main
m1 = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
    ]
m2 = [
    [1,3,4,8],
    [3,2,2,4],
    [5,7,1,9],
    [2,3,2,3]
    ]
obj1 = Backtracking(m1)
obj1.logic()
print "\n"
obj2 = Backtracking(m2)
obj2.logic()
print "\n"
obj3 = DP()
obj3.minPathSum(m1)
print "\n"
obj4 = DP()
obj4.minPathSum(m2)

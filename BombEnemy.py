#Bomb Enemy
#Difficulty:Medium
#
#Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
#The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
#Note that you can only put the bomb at an empty cell.
#
#Example:
#For the given grid
#
#0 E 0 0
#E 0 W E
#0 E 0 0
#
#return 3. (Placing a bomb at (1,1) kills 3 enemies)

class Approch1(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.output = [[0 for col in range(len(matrix[0]))]for row in range(len(matrix))]
        self.killMax = 0
        self.rowMax = None
        self.colMax = None

    def updateOutput(self, matrixCell, enemy, row, col):
        if matrixCell == "E":
            return enemy+1
        if matrixCell == "W":
            return 0
        self.output[row][col] = enemy+self.output[row][col]
        #save max
        if (self.killMax < self.output[row][col]):
            self.killMax = self.output[row][col]
            self.rowMax = row
            self.colMax = col
        return enemy

    def logic(self):
        #scan row from left to right
        for row in range(len(self.matrix)):
            enemy = 0
            for col in range(len(self.matrix[0])):
                enemy = self.updateOutput(self.matrix[row][col], enemy, row, col)
        #scan row from right to left
        for row in range(len(self.matrix)):
            enemy = 0
            for col in range(len(self.matrix), -1, -1):
                enemy = self.updateOutput(self.matrix[row][col], enemy, row, col)
        #Scan column from up to down
        for col in range(len(self.matrix[0])):
            enemy = 0
            for row in range(len(self.matrix)):
                enemy = self.updateOutput(self.matrix[row][col], enemy, row, col)
        #Scan column from down to up
        for col in range(len(self.matrix[0])):
            enemy = 0
            for row in range(len(self.matrix)-1, -1, -1):
                enemy = self.updateOutput(self.matrix[row][col], enemy, row, col)
        print "The row and col where max enemies will be killed is ",
        print self.rowMax, self.colMax
                
        

#Main Program
m = [[0, "E", 0, 0],
["E", 0, "W", "E"],
[0, "E", 0, 0]]
o = Approch1(m)
o.logic()

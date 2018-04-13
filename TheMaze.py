#The maze
#https://leetcode.com/articles/the-maze/

#helper class that has some common functions
class helper(object):

    def __init__(self, inputMatrix, source, destination):
        self.inputMatrix = inputMatrix
        self.source = source
        self.destination = destination
        #Create output matrix of row and columns filled with 0s
        self.outputMatrix = [[0 for col in range(len(inputMatrix[0]))] for row in range(len(inputMatrix))]

    #Gives all valid moves for the current move avoiding borders of matrix and walls
    def possibleMoves(self, currentMove):
        output = []
        row = currentMove[0]
        col = currentMove[1]
        #up
        r = row - 1
        #if row is within bounds of maze matrix
        if(r >= 0):
            #if there is no wall there in maze
            if(self.inputMatrix[][]
        

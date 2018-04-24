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
            if(self.inputMatrix[r][col] == 0):
                output.append([r, col])
        #down
        r = row +1
        #if row is within bounds of the maze
        if(r < len(self.inputMatrix)):
            #if there is no wall
            if(self.inputMatrix[r][col] == 0):
                output.append([r, col])
        #right
        c = col +1
        if(c < len(self.inputMatrix[0])):
            if(self.inputMatrix[row][c] == 0):
                output.append([row, c])
        #left
        c = col -1
        if(c >=0):
            if(self.inputMatrix[row][c]==0):
                output.append([row, c])
        return output

    #returns if current move is valid
    def isValidMove(self, move, nextMove):
        possible_moves = self.possibleMoves(move)
        if (nextMove in possible_moves):
            return True
        return False
    
    #rolls in the given direction until it hits a wall and returns cell where it stops
    def roll(self, direction, pos):
        row = pos[0]
        col = pos[1]
        if(direction == "left"):
            #col -1
            while(self.isValidMove([row, col], [row, col-1])):
                col = col -1
            return [row, col]
        if(direction == "right"):
            #col +1
            while(self.isValidMove([row, col], [row, col+1])):
                col = col +1
            return [row, col]
        if(direction == "up"):
            #row -1
            while(self.isValidMove([row, col], [row-1, col])):
                row = row -1
            return [row, col]
        if(direction == "down"):
            #row +1
            while(self.isValidMove([row, col], [row+1, col])):
                row = row +1
            return [row, col]

class dfs(helper):

    def __init__(self, inputMatrix, source, destination):
        helper.__init__(self, inputMatrix, source, destination)
        self.directions = ['up', 'down', 'left', 'right']

    def logic(self, src , dest, sol, om):
        if(src == dest):
            print "Found solution"
            print sol
            for row in range(len(om)):
                print om[row]
            return
        #print src, sol
        for d in self.directions:
            after_roll = self.roll(d, src)
            if(after_roll != src and om[after_roll[0]][after_roll[1]] == 0):
                om[after_roll[0]][after_roll[1]] = 1
                sol.append(d)
                self.logic(after_roll, dest, sol, om)
                #Backtracking
                sol.pop()
                om[after_roll[0]][after_roll[1]] = 0
                

    def solution(self):
        self.outputMatrix[self.source[0]][self.source[1]] = 1
        self.logic(self.source, self.destination, [], self.outputMatrix)

    

            

#Main Program
m = [[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0]]
s = [0,4]
d = [4,4]
h = dfs(m,s,d)
h.solution()

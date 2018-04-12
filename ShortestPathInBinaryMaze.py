#Shortest path in a Binary Maze
#https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/
#for sake of simplicity lets assume that only up, down, left and right are allowed.

class base(object):
    #this class holds all the common functions that are used between backtracking solution and
    #dynamic programming solution.
    #since dynamic programming is nothing but backtracking with memory

    def __init__(self, inputMatrix):
        #Create output matrix of row and columns filled with 0s
        self.outputMatrix = [[0 for col in range(len(inputMatrix[0]))] for row in range(len(inputMatrix))]

    #This function gives the list of all possible moves that can be taken next
    def isValidMove(self, s, totalRows, totalCols):
        output = []
        row = s[0]
        col = s[1]
        #up
        r = row-1
        if(r >= 0):
            output.append([r, col])
        #down
        r = row+1
        if(r < totalRows):
            output.append([r, col])
        #left
        c = col -1
        if(c >= 0):
            output.append([row, c])
        #right
        c = col +1
        if(c < totalCols):
            output.append([row, c])
        return output

    #function to print matrix
    def display(self, m):
        for i in range(len(m)):
            print m[i]


#Backtracking solution
class backTrack(base):

    def __init__(self, inputMatrix, source, destination):
        self.inputMatrix = inputMatrix
        self.source = source
        self.destination = destination
        #Create output matrix of row and columns filled with 0s
        base.__init__(self, inputMatrix)

    def bar(self, om, s, d, numberOfMoves):
        if(s == d):
            self.display(om)
            print "Number of Moves "+str(numberOfMoves)
            return
        validMoves = self.isValidMove(s, len(self.inputMatrix), len(self.inputMatrix[0]))
        for move in validMoves:
            #if the matrix has 1 in the move row and column only then can we proceed
            if(self.inputMatrix[move[0]][move[1]] == 1):
                #Next we haven't already been to that cell before
                if(om[move[0]][move[1]] != 1):
                    #visit that cell
                    om[move[0]][move[1]] = 1
                    self.bar(om, move, d, numberOfMoves+1)
                    #backtrack
                    om[move[0]][move[1]] = 0       

    def foo(self):
        #mark solution as 1 in output matrix
        self.outputMatrix[self.source[0]][self.source[1]] = 1
        self.bar( self.outputMatrix, self.source, self.destination, 0)
        print " now if you really think about it, this approach uses depth first search"
        
class bfs(base):
    def __init__(self, inputMatrix, source, destination):
        self.inputMatrix = inputMatrix
        self.source = source
        self.destination = destination
        #Create output matrix of row and columns filled with 0s
        base.__init__(self, inputMatrix)
        self.q = []
    
    def bar(self):
        #while the q is not empty
        while(self.q):
            #get the top move
            top = self.q.pop(0)
            print "current move "+str(top)
            #is top == destination ?
            if(top == self.destination):
                self.display(self.outputMatrix)
                return
            #find all valid moves for the current move
            validMoves = self.isValidMove(top, len(self.inputMatrix), len(self.inputMatrix[0]))
            #insert all valid moves in q
            for move in validMoves:
                #the move should be 1 in input matrix
                if(self.inputMatrix[move[0]][move[1]] == 0):
                    continue
                #this move is not already made in  output matrix
                if(self.outputMatrix[move[0]][move[1]] != 0):
                    continue
                #mark the cells visited
                self.outputMatrix[move[0]][move[1]] = 1
                self.q.append(move)

    def foo(self):
        #put source in q
        self.q.append(self.source)
        #Mark it in output matrix
        self.outputMatrix[self.source[0]][self.source[1]] = 1
        self.bar()
        print "bfs is giving wrong answer"
        
        

    
#Main program
m = [ [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]
    ]
source = [0,0]
destination = [3,4]
#bt = backTrack(m, source, destination)
#bt.foo()
dp = bfs(m, source, destination)
dp.foo()

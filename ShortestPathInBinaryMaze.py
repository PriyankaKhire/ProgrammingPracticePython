#Shortest path in a Binary Maze
#https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/
#for sake of simplicity lets assume that only up, down, left and right are allowed.
#Backtracking solution

#This function gives the list of all possible moves that can be taken next
def isValidMove(s, totalRows, totalCols):
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
def display(m):
    for i in range(len(m)):
        print m[i]
    
def bar(m, om, s, d, numberOfMoves):
    if(s == d):
        print "*****"
        display(om)
        print "Number of Moves "+str(numberOfMoves)
        print "*****"
        return
    validMoves = isValidMove(s, len(m), len(m[0]))
    for move in validMoves:
        #if the matrix has 1 in the move row and column only then can we proceed
        if(m[move[0]][move[1]] == 1):
            #Next we haven't already been to that cell before
            if(om[move[0]][move[1]] != 1):
                #visit that cell
                om[move[0]][move[1]] = 1
                bar(m, om, move, d, numberOfMoves+1)
                #backtrack
                om[move[0]][move[1]] = 0           

def foo(m, s, d):
    #Create output matrix of row and columns filled with 0s
    outputMatrix = [[0 for col in range(len(m[0]))] for row in range(len(m))]
    #mark solution as 1
    outputMatrix[s[0]][s[1]] = 1
    bar(m, outputMatrix, s, d, 0)
    
    
    

#Main Program
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
#print isValidMove([len(m)-1,len(m[0])-2], len(m), len(m[0]))
foo(m, source, destination)

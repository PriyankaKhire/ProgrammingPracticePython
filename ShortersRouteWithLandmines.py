#Find shortest safe route in a path with landmines

#Given a path in the form of a rectangular matrix having few landmines arbitrarily placed (marked as 0),
#calculate length of the shortest safe route possible from any cell in the first column to any cell
#in the last column of the matrix. We have to avoid landmines and their
'''four adjacent cells (left, right, above and below) '''#as they are also unsafe.
#We are allowed to move to only adjacent cells which are not landmines.
#i.e. the route cannot contains any diagonal moves.

sl = 0

def isSafe(i, j, maze, rowLen, colLen, sol):
    #If i and j are in bound
    if( 0 > i or i >= rowLen):
        return False
    if(0>j or j >= colLen):
        return False
    #Does not exist in solution array, meaning not visited already
    if(sol[i][j] == 1):
        return False
    #Not a mine
    if(maze[i][j] == 0):
        return False
    ''' We have to avoid landmines and their four adjacent cells (left, right, above and below) '''
    #Diagonally down mine : Left side
    #if(i+1 < rowLen and j+1 < colLen and maze[i+1][j+1] == 0):
        #return False
    #Diagonally up mine: right side
    #if( i-1 >= 0 and j-1 >= 0 and maze[i-1][j-1] == 0 ):
        #return False
    #Diagonally down mine : right side
    #if( i+1 < rowLen and j-1 >= 0 and maze[i+1][j-1] == 0 ):
        #return False
    #Diagonally up mine: Left side
    #if(  i-1 >= 0 and j+1 < colLen and maze[i-1][j+1] == 0):
        #return False
    #down
    if(  i+1 < rowLen and maze[i+1][j] == 0):
        return False
    #up
    if(  i-1 >= 0 and maze[i-1][j] == 0):
        return False
    #left
    if(  j+1 < colLen and maze[i][j+1] == 0):
        return False
    #right
    if(  j-1 >= 0 and maze[i][j-1] == 0):
        return False
    return True

def findPath(maze, sol, solLen, r, c, rowLen, colLen):
    global sl
    if(c == (colLen-1)):
        sl = solLen
        return True
    print "row :"+str(r)+" col :"+str(c)+" solution length :"+str(solLen)
    row_move = [0,0,1,-1]
    col_move = [1,-1,0,0]
    for k in range(len(row_move)):
        new_row = r+row_move[k]
        new_col = c+col_move[k]
        print "i: "+str(new_row)+" j: "+str(new_col)+" is Safe ?"+str(isSafe(new_row, new_col,maze, rowLen, colLen, sol))
        if(isSafe(new_row, new_col,maze, rowLen, colLen, sol)):
            sol[new_row][new_col] = 1
            for k in range(rowLen):
                print sol[k]
            if (findPath(maze, sol, solLen+1, new_row, new_col, rowLen, colLen)):
                return True
            else:
                #Backtrack
                sol[new_row][new_col] = 0
                for k in range(rowLen):
                    print sol[k]

def foo(maze, rowLen, colLen):
    #Find first safe cell
    mainSolution = 999
    s = []
    for r in range(rowLen):
        sol = [[0 for i in range(col)] for j in range(row)]
        if(isSafe(r, 0, maze, rowLen, colLen, sol)):            
            sol[r][0] = 1
            if(findPath(maze, sol, 1, r, 0, rowLen, colLen)):
                #Compare the path to previoulsy slelcted path
                print "Found a solution"
                if(mainSolution > sl):
                    print "this solution is better than previously found solutions"
                    mainSolution = sl
                    s = sol
                    print sl
                    for k in range(rowLen):
                        print sol[k]
                    print "*****"
            else:
                print "No solution exists for col = 0 and row = "+str(r)
                sol[r][0] = 0
    print "\n\n*****$$$$$*****"
    print "The smallest path is of length "+str(sl)
    print "The solution maze is"
    for k in range(rowLen):
        print s[k]
    print "*****$$$$$*****"
                

#Main Program
row = 12
col = 10
maze = [
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1 ],
    [ 1,  0,  1,  1,  1,  1,  1,  1,  1,  1 ],
    [ 1,  1,  1,  0,  1,  1,  1,  1,  1,  1 ],
    [ 1,  1,  1,  1,  0,  1,  1,  1,  1,  1 ],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1 ],
    [ 1,  1,  1,  1,  1,  0,  1,  1,  1,  1 ],
    [ 1,  0,  1,  1,  1,  1,  1,  1,  0,  1 ],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1 ],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1 ],
    [ 0,  1,  1,  1,  1,  0,  1,  1,  1,  1 ],
    [ 1,  1,  1,  1,  1,  1,  1,  1,  1,  1 ],
    [ 1,  1,  1,  0,  1,  1,  1,  1,  1,  1 ]
    ]
foo(maze, row, col)

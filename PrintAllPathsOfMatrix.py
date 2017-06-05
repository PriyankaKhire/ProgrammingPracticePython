#Print all possible paths from top left to bottom right of a mXn matrix
#http://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/

def isSafe(row, col, m, n):
    #Check bounds
    if not (0<= row and row < m):
        return False
    if not (0<= col and col < n):
        return False
    return True


def foo(matrix, row, col, paths, m, n):
    #print "row "+str(row)+" col "+str(col)
    #print "paths so far "+str(paths)
    if (row == (m-1) and col == (n-1)):
        print paths
        return
    moves_x = [0,1]
    moves_y = [1,0]
    for i in range(len(moves_x)):
        #print "is moving safe ?"+str(isSafe(row+moves_x[i], col+moves_y[i], m, n))
        if(isSafe(row+moves_x[i], col+moves_y[i], m, n)):
            paths.append(matrix[row+moves_x[i]][col+moves_y[i]])
            if(foo(matrix, row+moves_x[i], col+moves_y[i], paths, m, n)):
                return True
            else:
                #Backtrack
                paths.pop()

#MainProgram
matrix = [
    [1,2,3],
    [4,5,6]
    ]                
foo(matrix, 0, 0, [1], 2, 3)

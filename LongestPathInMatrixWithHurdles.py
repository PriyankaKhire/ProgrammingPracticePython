#Longest Possible Route in a Matrix with Hurdles
#http://www.geeksforgeeks.org/longest-possible-route-in-a-matrix-with-hurdles/

path_len = 0

def isSafe(row, col, matrix, m, n, path):
    #Check bounds
    if not ( 0<= row and row < m):
        return False
    if not (0<= col and col < n):
        return False
    #Check for cycles
    if( [row, col] in path):
        return False
    #Check for hurdles
    if(matrix[row][col] == 0):
        return False
    return True

def foo(matrix, m, n, path, pathLen, row, col):
    print "path so far "+str(path)
    print "path length so far "+str(pathLen)
    print "curr row "+str(row)
    print "curr col "+str(col)
    global path_len
    if (pathLen > path_len):
        path_len = pathLen
        print "Longest path so far "+str(pathLen)
    #All possible moves
    moves_x = [1, -1, 0, 0]
    moves_y = [0, 0, 1, -1]
    for i in range(len(moves_x)):
        print "is next move safe ? "+str(isSafe(row+moves_x[i], col+moves_y[i],  matrix, m, n, path))
        if(isSafe(row+moves_x[i], col+moves_y[i],  matrix, m, n, path)):
            path.append([row+moves_x[i], col+moves_y[i]])
            if(foo(matrix, m, n, path, pathLen+1, row+moves_x[i], col+moves_y[i])):
                return True
            else:
                #Backtrack
                print "Backtracking "
                path.pop()


#main Program
matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
m = 3
n = 10
foo(matrix, m, n, [], 0, 0, 0)

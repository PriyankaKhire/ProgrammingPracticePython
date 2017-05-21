#Find paths from corner cell to middle cell in maze

#Given a square maze containing positive numbers, find all paths from a corner cell
#(any of the extreme four corners) to the middle cell. We can move exactly n steps
#from a cell in 4 directions i.e. North, East, West and South where n is value of the cell.

#We can move to mat[i+n][j], mat[i-n][j], mat[i][j+n], and mat[i][j-n] from a cell mat[i][j]
#where n is value of mat[i][j].

def isSafe(path, maze, result):
    i = path[0]
    j = path[1]
    if not (0<= i and i < len(maze)):
        return False
    if not(0<= j and j < len(maze)):
        return False
    if path in result:
        return False
    return True

def calculatePaths(i,j,x):
    result = []
    result.append([i+x,j])
    result.append([i-x,j])
    result.append([i,j+x])
    result.append([i,j-x])
    return result

def findPath(i,j,n,maze, result):
    if(i == n and j == n):
        print "found mid"
        print result
        return True
    print "I is "+str(i)+" J is "+str(j)
    paths = calculatePaths(i,j,maze[i][j])
    for path in paths:
        print path
        if(isSafe(path, maze, result)):
            print "Path "+str(path)+" is safe"
            #Add path to result
            result.append(path)
            print "Result so far is "+str(result)
            if(findPath(path[0], path[1], n, maze, result)):
                return True
            else:
                #BackTrack
                print "*****BackTracking*****"
                result.pop()
                print "Result now is "+str(result)

def foo(maze):
    #Find mid
    n = 0
    if len(maze) % 2 == 0:
        n = len(maze)/2
    else:
        n = (len(maze)/2)+1
    findPath(0,0,n,maze, [])

#Main Program
maze = [
    [ 3, 5, 4, 4, 7, 3, 4, 6, 3 ],
    [ 6, 7, 5, 6, 6, 2, 6, 6, 2 ],
    [ 3, 3, 4, 3, 2, 5, 4, 7, 2 ],
    [ 6, 5, 5, 1, 2, 3, 6, 5, 6 ],
    [ 3, 3, 4, 3, 0, 1, 4, 3, 4 ],
    [ 3, 5, 4, 3, 2, 2, 3, 3, 5 ],
    [ 3, 5, 4, 3, 2, 6, 4, 4, 3 ],
    [ 3, 5, 1, 3, 7, 5, 3, 6, 4 ],
    [ 6, 2, 4, 3, 4, 5, 4, 5, 1 ]
    ]
foo(maze)

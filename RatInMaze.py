#Rat in a Maze

#size of the matrix
N = 4
#Solution array
sol = [[0 for i in range(N)] for j in range(N)]

def isSafe_x(i,j,p):
    i +=1
    if(0<=i and i<N and p[i][j] == 1):
        return True
    else:
        return False

def isSafe_y(i,j,p):
    j +=1
    if(0<=j and j<N and p[i][j] == 1):
        return True
    else:
        return False

def foo(i,j,p):
    #Retrun condition
    if(i == N-1 and j == N-1 and p[i][j] == 1):
        print "found the way"
        print sol
        return True
    if(0<=i and i<N and 0<=j and j<N):
        if(isSafe_x(i,j,p)):
            #make a move
            i += 1
            sol[i][j] = 1
            if(foo(i,j,p)):
                return True
            else:
                sol[i][j] = 0
                i -= 1
        elif(isSafe_y(i,j,p)):
            j += 1
            sol[i][j] = 1
            if(foo(i,j,p)):
                return True
            else:
                sol[i][j] = 0
                j -= 1
        else:
            return False

#Main Program
p = [[1, 0, 0, 0],
     [1, 1, 0, 1],
     [0, 1, 0, 0],
     [1, 1, 1, 1]]
sol[0][0] = 1
foo(0,0,p)

sol = [[0 for i in range(N)] for j in range(N)]
p = [[1, 1, 1, 1],
     [0, 1, 0, 1],
     [0, 0, 0, 1],
     [0, 0, 0, 1]]
sol[0][0] = 1
foo(0,0,p)


                
                

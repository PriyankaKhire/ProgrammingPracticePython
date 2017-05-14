# N QUEENS
N = 4
Q = [[0 for i in range(N)] for j in range(N)]

def isSafe(row, col):
    #Search horizontally AND vertically
    for j in range(N):
        if(Q[row][j] == 1):
            return False
        if(Q[j][col] == 1):
            return False
    #Search diagonally
    for i in range(1,N):
        if(row+i > 0 and row+i < N):
            if(col+i > 0 and col+i < N):
                if(Q[row+i][col+i] == 1):
                    return False
            if(col-i > 0 and col-i < N):
                if(Q[row+i][col-i] == 1):
                    return False
        if(row-i > 0 and row-i < N):
            if(col+i > 0 and col+i < N):
                if(Q[row-i][col+i] == 1):
                    return False
            if(col-i > 0 and col-i < N):
                if(Q[row-i][col-i] == 1):
                    return False

def nQueens(n):
    if (n == 0):
        for i in range(N):
            print Q[i]
        return True
    #Start placing the queens
    for i in range(N):
        for j in range(N):
            print "***"
            print "Queen number "+str(n)
            print "I ="+str(i)+" J="+str(j)
            print isSafe(i,j)
            print Q
            print "***"
            if(Q[i][j] == 0):
                if(isSafe(i,j) != False):
                    Q[i][j] = 1
                    if(nQueens(n-1)):
                        return True
                    else:
                        #Else backtrack
                        print "***Backtracking***"
                        Q[i][j] = 0

#The minot tweek that we did in this methode was that we incremented col
#We can do this even by incrementing the row
#why did this work better ?
#Both are same programs i.e. nQueens_methode2 and nQueens
#but here by incrementing the col we are elemenating the excess checking of that same col
#when we know that, that col is any ways isSafe is going to be false.
def nQueens_methode2(n, col):
    if (n == 0):
        for i in range(N):
            print Q[i]
        return True
    #Start placing the queens
    for i in range(N):
        print "***"
        print "Queen number "+str(n)
        print "I ="+str(i)+" col = "+str(col)
        print isSafe(i,col)
        print Q
        print "***"
        if(Q[i][col] == 0):
            if(isSafe(i,col) != False):
                Q[i][col] = 1
                if(nQueens_methode2(n-1, col+1)):
                    return True
                else:
                    #Else backtrack
                    print "***Backtracking***"
                    Q[i][col] = 0



nQueens_methode2(N, 0)

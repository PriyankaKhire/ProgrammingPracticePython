#Knight's tour proablem
#The knight is placed on the first block of an empty board and, moving according to the rules of chess, must visit each square exactly once.

#At a given point of time a knight can have the following possible moves
# let i be row and j be column
#A knight can make following moves if the new i and j are  0 <= i <= 64 and 0 <= j 64
#the moves are:
# i+2, j+1
# i+2, j-1
# i-2, j+1
# i-2, j-1
# i+1, j+2
# i+1, j-2
# i-1, j+2
# i-1, j-2
#These moves are represented by move_x and move_y mattirx

#To proceed first check if the following chess_board[i][j] is = Unassigned or not
#if it is then calculate the new i and j and if new i and j are satisfying the conditions then assign
#count to chess_board[i][j] else back track

#This matrix specifies the next move for knight
move_x = [2, 1, -1, -2, -2, -1,  1,  2]
move_y = [1, 2,  2,  1, -1, -2, -2, -1]

def display():
    for i in range(8):
        print cb[i]

def break_point():
    display()
    exit(1)
        

def isSafe(cb,i,j,k):
    i += move_x[k]
    j += move_y[k]
    #print "In isSafe k = "+str(k)+" i = "+str(i)+" j = "+str(j)
    if(0 <= i and i < 8) and (0<= j and j < 8)  and(cb[i][j] == -1):
        return True
    else:
        return False


def foo1(cb, i, j, count):
    if(cb[i][j] == -1 and count < 64):
        for k in range(8):
            print "k = "+str(k)
            if(isSafe(cb, i, j, k)):
                count += 1
                i += move_x[k]
                j += move_y[k]
                cb[i][j] = count
                if(foo1(cb, i, j, count)):
                    return True
                else:
                    count -= 1
                    i -= move_x[k]
                    j -= move_y[k]
                    cb[i][j] = -1
    display()

def foo(cb,i,j, count):
    #print "*****"
    #print "row = "+str(i)
    #print "col = "+str(j)
    #print "count = "+str(count)
    #display()
    #print  ""
    #Break Point
    if count == 64:
        break_point()
    if(count < 64):
        #Begin the code
        for k in range(8):
            #print "k = "+str(k)
            if(isSafe(cb,i,j,k)):
                #Update the count
                #print "count = "+str(count)
                count += 1
                #print "count = "+str(count)
                #Update new i and j
                i += move_x[k]
                j += move_y[k]
                #Update the board
                cb[i][j] = count
                #print "row = "+str(i)+" col = "+str(j)+" count = "+str(count)
                #display()
                #print "*****"
                if(foo(cb, i,j,count)):
                    return True
                else:
                    #BACKTRACK
                    #print "$$$$$$$BACKTRACKING$$$$$$$$$$"
                    cb[i][j] = -1
                    i -= move_x[k]
                    j -= move_y[k]
                    count -= 1
        return False
    else:
        return False

#Main program
cb = [[-1 for i in range(8)] for j in range(8)]
#foo(cb,0,0,0)

#*******************************************************************************************
#*******************************************************************************************

#New program
def calculate_move(row, col):
    r = [0 for i in range(8)]
    c = [0 for i in range(8)]
    rw = row +2
    r[0] = rw
    r[7] = rw
    rw = row - 2
    r[3] = rw
    r[4] = rw
    rw = row +1
    r[1] = rw
    r[6] = rw
    rw = row -1
    r[2] = rw
    r[5] = rw
    cl = col +2
    c[1] = cl
    c[2] = cl
    cl = col -2
    c[5] = cl
    c[6] = cl
    cl = col +1
    c[0] = cl
    c[3] = cl
    cl  = col -1
    c[4] = cl
    c[7] = cl
    return r, c

def isSafe(row, col):
    if not(0<= row and row <= 7):
        return False
    if not(0<= col and col <= 7):
        return False
    if not(cb[row][col] == -1):
        return False
    return True

def foo(row, col, move):
    if(move == 64):
        return True
    r,c = calculate_move(row,col)
    for i in range(8):
        print "Move number "+str(move)
        print "move r =  "+str(r[i])+" move c = "+str(c[i])
        print "isSafe ? "+str(isSafe(r[i],c[i]))
        if(isSafe(r[i],c[i])):
            cb[r[i]][c[i]] = move
            for j in range(8):
                print cb[j]
            if(foo(r[i],c[i], move+1) == True):
                return True
            else:
                print "*** Back Tracking ***"
                cb[r[i]][c[i]] = -1

cb[0][0] = 0
foo(0,0,1)

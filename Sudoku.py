#Sudoku

#Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9)
#to the empty cells so that every row, column, and subgrid of size 3×3 contains exactly one
#instance of the digits from 1 to 9.

#Global variables
'''
n = 9
s = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
    ]
'''
n = 4
s = [
    [1,0,3,0],
    [0,0,2,1],
    [0,1,0,2],
    [2,4,0,0]
    ]
def next_row_col(row, col):
    col += 1
    if(col == n):
        row +=1
        col = 0
    if(row == n):
        return n,n
    return row, col

#For sudoku 9x9
'''
def tiny_box_i_range(i):
    #i between 0 to 2: first box
    if(0<=i and i<=2):
        return 0,2
    #i between 3 to 5: second box
    if(3<=i and i<=5):
        return 3,5
    #i between 6 to 8: third box
    if(6<=i and i<=8):
        return 6,8
'''
#For sudoku 4x4
def tiny_box_i_range(i):
    #i between 0 to 1: first box
    if(0<=i and i<=1):
        return 0,1
    #i between 2 to 3: second box
    if(2<=i and i<=3):
        return 2,3

def tiny_box_range(row, col):
    xRangeLow, xRangeHigh = tiny_box_i_range(row)
    yRangeLow, yRangeHigh = tiny_box_i_range(col)
    return xRangeLow, xRangeHigh, yRangeLow, yRangeHigh

def isSafe(num, row, col):
    for i in range(n):
        #Check for number horizontally
        if(s[row][i] == num):
            return False
        #Check for number vertically
        if(s[i][col] == num):
            return False
    #Check for number in 3x3 box
    xRangeLow, xRangeHigh, yRangeLow, yRangeHigh = tiny_box_range(row, col)
    for i in range(xRangeLow, xRangeHigh+1):
        for j in range(yRangeLow, yRangeHigh+1):
            if(s[i][j] == num):
                return False
    return True    

def foo(row, col):
    #Return condition
    if(row == n and col == n):
        print s
        exit()
    print "Row = "+str(row)+" Col = "+str(col)
    prevRow = row
    prevCol = col
    if(s[row][col] == 0):
        for i in range(1,n+1):
            print "is "+str(i)+" safe ? "+str(isSafe(i, row, col)) 
            if(isSafe(i, row, col)):
                s[row][col] = i
                row, col = next_row_col(row, col)
                if(foo(row, col)):
                    return True
                else:
                    print "***Back Tracking***"
                    row = prevRow
                    col = prevCol
                    #Backtrack
                    s[row][col] = 0
                    print "Row = "+str(row)+" Col = "+str(col)
    else:
        row, col = next_row_col(row, col)
        foo(row, col)
            
#Main Program
foo(0,0)
                

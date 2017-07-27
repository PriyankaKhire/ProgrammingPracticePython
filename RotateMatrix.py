#transpose matrix 
def foo(m, n):
    row = 0
    col = row+1
    while(row < n-1-1):
        if(col == n):
            row +=1
            col = row+1
        #Swap
        m[row][col], m[col][row] = m[col][row], m[row][col]
        col +=1
    print m

#Main Program
m  = [[1,2,3],[4,5,6],[7,8,9]]
print m
foo(m, 3)

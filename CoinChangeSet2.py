#Find minimum number of coins that make a given value
#Given a value V, if we want to make change for V cents, and we have infinite supply
#of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?
def createMatrix(n, s):
    m = [[ 0 for col in range(n+1)] for row in range(len(s)+1)]
    return m

def foo(n, s):
    matrix = createMatrix(n,s)
    for row in range(len(s)):
        for col in range(n+1):
            if(s[row] == col):
                matrix[row+1][col] = 1
            elif(s[row] > col):
                #Copy the value from top
                matrix[row+1][col] = matrix[row][col]
            else:
                #Get the value from those many steps behind
                value = matrix[row+1][col - s[row]]
                #If this value is 0 then get the value form top
                if value == 0:
                    matrix[row+1][col] = matrix[row][col]
                if(value > 0):
                    #Find top value
                    top = matrix[row][col]
                    if top == 0:
                        matrix[row+1][col] = value+1
                    else:
                        matrix[row+1][col] = min(top, value+1)
    print matrix
    print "we need a minimum of "+str(matrix[len(s)][n])

#Main Program
foo(10, [2,5,3,6])
foo(30, [25, 10, 5])
foo(11, [9, 6, 5, 1])

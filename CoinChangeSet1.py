#Coin change
#Given a value N, if we want to make change for N cents, and we have infinite supply
#of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change?
#The order of coins doesn’t matter.

#For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
#So output should be 4. For N = 10 and S = {2, 5, 3, 6},
#there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
def createMatrix(n,s):
    m = [[0 for col in range(n+1)] for row in range(len(s)+1)]
    #Fill first col with 1
    for row in range(len(s)+1):
        m[row][0] = 1
    return m

def foo(n, s):
    matrix = createMatrix(n, s)
    for row in range(len(s)):
        for col in range(n+1):
            if(col < s[row]):
                #Copy value from the top
                matrix[row+1][col] = matrix[row][col]
            else:
                #add the value from top and s[row] steps behind
                #why do we move those s[row] steps behind ?
                #coz there is a multiple of s[row] those many steps behind and if there isnt then we still get the correct value
                matrix[row+1][col] = matrix[row][col]+matrix[row+1][col-s[row]]
    print matrix
    print "So the total number of ways to make the change is "+str(matrix[len(s)][n])

#Main Program
foo(10, [6, 2, 5, 3])
foo(4, [1,2,3])

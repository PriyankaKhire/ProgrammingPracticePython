#Egg Dropping Puzzle
#http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle/
def createMatrix(eggs, floors):
    m = [[ 0 for col in range(floors+1)] for row in range(eggs+1)]
    #Fill first floor row 
    for col in range(floors+1):
        m[1][col] = col
    return m

def foo(eggs, floors):
    matrix = createMatrix(eggs, floors)
    for row in range(2, eggs+1):
        for col in range(floors+1):
            if(row > col):
                #copy value from the top
                matrix[row][col] = matrix[row-1][col]
            else:
                minimum = 999
                print "eggs = "+str(row)+" floor = "+str(col)
                for i in range(1, col):
                    print "if egg breaks "+str(matrix[row-1][i-1])
                    print "if egg does't break "+str(matrix[row][col-i])
                    val = 1+max(matrix[row-1][i-1], matrix[row][col-i])
                    minimum = min(val, minimum)
                matrix[row][col] = minimum
                print "answer is "+str(matrix[row][col])
                print 
    print matrix

                
#Main Program
foo(2, 6)
foo(2, 36)

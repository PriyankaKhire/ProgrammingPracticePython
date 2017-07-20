#Cutting a Rod
#http://www.geeksforgeeks.org/dynamic-programming-set-13-cutting-a-rod/
def createMatrix(p):
    m = [[0 for col in range(p)] for row in range(p)]
    return m

def foo(price):
    matrix = createMatrix(len(price))
    for row in range(len(price)):
        for col in range(len(price)):
            if(row > col):
                #Copy the value from top
                if row !=0:
                    matrix[row][col] = matrix[row-1][col]
            else:
                if row !=0:
                    matrix[row][col] = max(matrix[row-1][col], price[row]+matrix[row][col-row])
    for i in range(len(price)):
        print matrix[i]
    print "The maximum obtainable value is "+str(matrix[len(price)-1][len(price)-1])

#Main Program
foo([0, 1, 5, 8, 9, 10, 17, 17, 20])
foo([0, 3,   5,   8 ,  9,  10,  17,  17,  20])


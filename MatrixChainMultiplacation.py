#Matrix Chain Multiplication

#http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
def createMatrix(m):
    return [[0 for col in range(len(m))] for row in range(len(m))]

def foo(m):
    solMatrix = createMatrix(m)
    length = 1
    row = 0
    col = length
    while(length < len(m)):
        row = 0
        col = length
        while(col < len(m)):
            #if row and col are consequitive then
            if (col = row +1):
                solMatrix[row][col] = m[row][0]*m[row][1]*m[col][1]
            row +=1
            col +=1
        #Previous col additions of same row plus this cell
        #solMatrix[row][col] =
        length +=1


#Main Program
foo([[2,3],[3,6],[6,4],[4,5]])

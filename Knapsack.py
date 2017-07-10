# 0/1 Knapsack proablem

def getWeights(m, weight, totalWeight):
    row = len(weight)
    col = totalWeight
    result = []
    while(row > 0 and col > 0):
        if (m[row][col] == m[row-1][col]):
            #Go up
            row -= 1
            continue
        else:
            result.append(weight[row-1])
            row -=1
            col -= weight[row]
    print "The weights are "+str(result)

def createMatrix(weight, totalWeight):
    m = [[0 for col in range(totalWeight+1)] for row in range(len(weight)+1)]
    return m

def foo(weight, value, totalWeight):
    matrix = createMatrix(weight, totalWeight)
    #Fill first row
    for col in range(totalWeight+1):
        if(weight[0] <= col):
            matrix[1][col] = weight[0]
    for row in range(1, len(weight)):
        for col in range(totalWeight+1):
            #when weight is greater than col values then just copy the top values
            if(weight[row] > col):
                matrix[row+1][col] = matrix[row][col]
            else:
                matrix[row+1][col] = max(matrix[row][col] , value[row]+matrix[row+1][col-weight[row]])
    print "The max value is "+str(matrix[len(weight)][totalWeight])
    for row in range(len(weight)+1):
        print matrix[row]
    getWeights(matrix, weight, totalWeight)

#Main Program
foo([5,3,4,1], [7,4,5,1], 7)
foo([1,1,1],[10,20,30], 2)
foo([1,2,3],[6,10,12],5)

#Edit distance
def getEdits(m, s1, s2):
    print "The minimum edits required to change "+s1+" to "+s2+" are "+str(m[len(s2)-1][len(s1)-1])
    row = len(s2)-1
    col = len(s1)-1
    while(row >=0 and col>=0):
        if(s1[col] == s2[row]):
            #Go diagonally up
            col -=1
            row -=1
        else:
            if(m[row][col-1] < m[row-1][col-1] and m[row][col-1] < m[row-1][col]):
                print "Delete "+s1[col]+" from "+s1+" at position "+str(col)
                col -= 1
            elif(m[row-1][col] < m[row][col-1] and m[row-1][col] < m[row-1][col-1]):
                print "Insert "+s2[row]+" into "+s1+" at position "+str(col+1)
                row -=1
            elif(m[row-1][col-1] < m[row][col-1] and m[row-1][col-1] < m[row-1][col]):
                print "Change "+s1[col]+" to "+s2[row]+" at position "+str(col)
                row -= 1
                col -= 1

def fill_first(m, s1, s2):
    #Fill first cell
    if(s1[0] == s2[0]):
        m[0][0] = 0
    else:
        m[0][0] = 1
    #Fill first row
    for col in range(1, len(s1)):
        if(s1[col] == s2[0]):
            m[0][col] = m[0][col-1]
        else:
            m[0][col] = 1 + m[0][col-1]
    #Fill first col
    for row in range(1, len(s2)):
        if(s2[row] == s1[0]):
            m[row][0] = m[row-1][0]
        else:
            m[row][0] = 1 + m[row-1][0]
    return m

def createMatrix(str1, str2):
    m = [[0 for col in range(str1)] for row in range(str2)]
    return m

def foo(str1, str2):
    matrix = createMatrix(len(str1), len(str2))
    #Fill first row and column
    matrix = fill_first(matrix, str1, str2)
    #Fill rest of the matrix
    for row in range(1, len(str2)):
        for col in range(1, len(str1)):
            if(str1[col] == str2[row]):
                #Get the value from the diagonal
                matrix[row][col] = matrix[row-1][col-1]
            else:
                matrix[row][col] = 1 + min(matrix[row][col-1], matrix[row-1][col], matrix[row-1][col-1])
    getEdits(matrix, str1, str2)

#Main Program
foo("geeks", "gesek")
foo("cut", "cat")
foo("pale", "ple")

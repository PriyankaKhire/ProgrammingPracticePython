#Edit distance
def getEdit(m, s1, s2):
    row = len(s2)
    col = len(s1)
    while(row > 0 and col > 0):
        #if letters are same we get the value from the diagonal
        if(s1[col-1] == s2[row-1]):
            row -=1
            col -=1
        else:
            #if diagonal is min then we edit
            if(m[row-1][col-1] < m[row][col-1] and m[row-1][col]):
                print "Edit "+s1[col-1]+" to "+s2[row-1]
                row -=1
                col -=1
                continue
            #if left is min then we delete
            if(m[row][col-1] < m[row-1][col-1] and m[row][col-1] < m[row-1][col]):
                print "Delete "+s1[col-1]
                col -=1
                continue
            # if up in min then we add
            if(m[row-1][col] < m[row-1][col-1] and m[row-1][col] < m[row][col-1]):
                print "add "+s2[row-1]
                row -=1
                continue
            

def createMatrix(m,n):
    m = [[0 for col in range(m)] for row in range(n)]
    return m

def foo(str1, str2):
    matrix = createMatrix(len(str1)+1, len(str2)+1)
    #Fill first rows
    for row in range(len(str2)+1):
        matrix[row][0] = row
    for col in range(len(str1)+1):
        matrix[0][col] = col
    #Start calculating
    for row in range(len(str2)):
        for col in range(len(str1)):
            #Take the value from the diagonal
            if(str2[row] == str1[col]):
                matrix[row+1][col+1] = matrix[row][col]
            else:
                #Take the min of 3 values and add 1 to it
                matrix[row+1][col+1] = min(matrix[row+1][col], matrix[row][col+1], matrix[row][col])+1
    for i in range(len(str2)+1):
        print matrix[i]
    print "Edit distance is "+str(matrix[len(str2)][len(str1)])
    getEdit(matrix, str1, str2)
    
    

#Main Program
foo("abcdef", "azced")
foo("geek", "geeks")
foo("cat", "cut")
#get edit Doesnt work for this case 
foo("sunday", "saturday")

def reverse(s):
    return s[::-1]

def printPalindrome(m, s):
    print "Length of the longest palindrome is "+str(m[0][len(s)-1])
    #Start from upper right corner
    row = 0
    col = len(s)-1
    result = ""
    while(col > 0 and row < len(s)):
        if m[row][col] == 0:
            break
        #Compare current cell with its down, left and diagonally down cell
        if(m[row][col] != m[row][col-1] and m[row][col] != m[row+1][col] and m[row][col] != m[row+1][col-1]):
            #add current row , col to output sequence
            print "adding "+s[row]
            result += s[row]
            row +=1
            col -=1
            continue
        elif(m[row][col] == m[row][col-1] and m[row+1][col] != m[row][col-1] and m[row+1][col-1] != m[row][col-1]):
            print "moving left"
            col -=1
            continue
        elif(m[row][col] ==m[row+1][col] and m[row][col-1] !=m[row+1][col] and m[row+1][col-1] !=m[row+1][col]):
            print "moving down"
            row +=1
            continue
        elif(m[row][col] == m[row+1][col-1] and m[row+1][col] != m[row+1][col-1] and m[row][col-1] != m[row+1][col-1]):
            print "moving diagonal"
            row +=1
            col -=1
            continue
    print "The result is"
    #If string length is even
    if(m[0][len(s)-1] %2 == 0):
        print result+reverse(result)
    else:
        print result+reverse(result[:-1])
            
    
def createMatrix(string):
    m = [[0 for col in range(len(string))] for row in range(len(string))]
    return m
def dp(string):
    matrix = createMatrix(string)
    #The matrix needs to be filled diagonally
    row = 0
    col = 0
    length = 0
    #This ensures that the matrix is filled diagonally, 1 diagonal at a time
    while(length < len(string)-1):
        if (row == len(string) or col == len(string)):
            row = 0
            length +=1
            col = length
        if (row == col):
            matrix[row][col] = 1
        else:
            if string[col] == string[row]:
                matrix[row][col] = 2+matrix[row+1][col-1]
            else:
                matrix[row][col] = max(matrix[row][col-1], matrix[row+1][col])
        row += 1
        col += 1
    for row in range(len(string)):
        print matrix[row]
    printPalindrome(matrix, string)

#Longest Palindromic sub sequence
def isPalindrome(string):
    for i in range(len(string)/2):
        if(string[i] != string[len(string)-1-i]):
            return False
    return True

#This prints all the palindromic substrings
def foo(string, index, result):
    if(isPalindrome(result)):
        print result
    for i in range(index, len(string)):
        result.append(string[i])
        if(foo(string, i+1, result)):
            return True
        result.pop()
    

#Main Program
#foo("aab", 0, [])
#foo("BBABCBCAB", 0, [])
dp("aab")
dp("agbdba")

#Longest common subsequence

#Gives position of a letter in string starting from a particular index
def pos(string, index, letter):
    return (string[index:].index(letter))

def isSafe(letter, string, result, index, letter_pos):
    if not letter in string[index:]:
        return False
    #if result is empty
    if not result:
        return True
    else:
        #find the position of this last letter in the string starting from index
        if(pos(string, index, letter)+index > letter_pos):
            return True
        else:
            return False
        
    
#Ok this one is buggy, it prints some common strings not all, i am guessing the problem is with is safe method
def backtracking(str1, str2, result, index1, index2):
    print result
    if((index1 == len(str1)) or (index2 == len(str2))):        
        return
    for i in range(index1, len(str1)):
        if(isSafe(str1[i], str2, result, index2, i)):
            result.append(str1[i])
            p = pos(str2, index2, str1[i])
            backtracking(str1, str2, result, i+1, index2+p+1)
            #backtrack
            result.pop()

def getSequence(str1, str2, res):
    result = ""
    i = len(str1)
    j = len(str2)
    while(i >=0  and j >= 0):
        #search up right and diagonally up
         #if current is the letter
        if(res[j][i] !=  res[j-1][i] and res[j][i] != res[j][i-1] and res[j][i] != res[j-1][i-1]):
            result += str2[j-1]
            #Go diagonal
            i -=1
            j-=1
            continue
        #if you got current letter from up
        if (res[j][i] == res[j-1][i]):
            #go up
            j -=1
            continue
        #if you got the current letter from right
        if(res[j][i] == res[j][i-1]):
            #Go right
            i-=1
            continue
    print result
    print "reverse this result"

#dynamic programming program understoop from tushar roy's video.
def dp(str1, str2):
    result = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                result[j+1][i+1] = result[j][i]+1
            else:
                result[j+1][i+1] = max(result[j+1][i], result[j][i+1])
    for i in range(len(str2)+1):
        print result[i]
    #Get the sequence
    getSequence(str1, str2, result)
#Main Program
#backtracking("abazdc", "bacbad", [], 0,0)
#print
#backtracking("bacbad", "abazdc", [], 0,0)
dp("AGGTAB", "GXTXAYB")
dp ("bacbad", "abazdc")

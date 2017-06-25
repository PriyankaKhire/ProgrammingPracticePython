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

#Main Program
backtracking("abazdc", "bacbad", [], 0,0)
print
backtracking("bacbad", "abazdc", [], 0,0)

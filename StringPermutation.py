#String Permutation Algorithm
#Using Tushar Roy's Backtracking Video

#Prints the permutation
def permute(count, string, result, letterCount):
    if letterCount == 0:
        print result
        return
    print count
    for i in range(len(string)):
        if(count[string[i]] > 0):
            count[string[i]] -= 1
            permute(count, string, result+string[i], letterCount-1)
            #Backtrack
            count[string[i]] += 1

#This function compresses the string and fills the count hash
def strCompress(count, string):
    #letterCount counts the total number of letters in string
    letterCount = 0
    for letter in string:
        letterCount += 1
        if(letter in count):
            count[letter] +=1
        else:
            count[letter] = 1
    compressedString = ""
    for k,v in count.items():
        compressedString += str(k)
    return count,compressedString, letterCount

#Supports strings with repeated characters
def bar(string):
    count = {}
    #Get  the character count
    count, compressedString, letterCount = strCompress(count, string)
    permute(count, compressedString, "", letterCount)
    

#Does not support strings with repeated characters like AABC
def foo(string, result):
    if string == "":
        print result
        return
    #print string
    for i in range(len(string)):
        #string[:i]+string[i+1:] => delets string at ith position
        foo(string[:i]+string[i+1:], result+string[i])

#Main Program
foo("ABCD","")
bar("AABC")

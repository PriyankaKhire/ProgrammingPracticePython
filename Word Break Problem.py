#Word Break Problem using Backtracking

#Given a valid sentence without any spaces between the words and a dictionary of valid English words,
#find ALL possible ways to break the sentence in individual dictionary words.

words = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango", "and"]

def findFirstOccourence(string, result):
    if (string == ""):
        print result
        return True
    word = ""
    for i in range(len(string)):
        word += string[i]
        if word in words:
            if(findFirstOccourence(string[i+1:], result+word+" ")):
                return True

def findAllOccourences(string, result):
    if (string == ""):
        print "\n\n\n"
        print result
        print "\n\n\n"
        return True
    word = ""
    print "Remaining string "+str(string)
    for i in range(len(string)):
        word += string[i]
        print "i = "+str(i)
        print "word = "+str(word)
        if word in words:
            print "word found in words"
            print "Result = "+str(result+word+" ")
            findAllOccourences(string[i+1:], result+word+" ")
        else:
            print "word not found in words"
    #Backtracking
    print "****Here is where you backtrack****"


#Main Program
findAllOccourences("ilikesamsungmobile", "")
findFirstOccourence("ilikeicecreamandmango", "")

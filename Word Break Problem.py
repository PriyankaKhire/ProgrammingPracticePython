#Word Break Problem using Backtracking

#Given a valid sentence without any spaces between the words and a dictionary of valid English words,
#find ALL possible ways to break the sentence in individual dictionary words.

class Approch1(object):

    def __init__(self):
        self.words = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango", "and"]

    def findFirstOccourence(self, string, result):
        if (string == ""):
            print result
            return True
        word = ""
        for i in range(len(string)):
            word += string[i]
            if word in self.words:
                if(self.findFirstOccourence(string[i+1:], result+word+" ")):
                    return True

    def findAllOccourences(self, string, result):
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
            if word in self.words:
                print "word found in words"
                print "Result = "+str(result+word+" ")
                self.findAllOccourences(string[i+1:], result+word+" ")
            else:
                print "word not found in words"
        #Backtracking
        print "****Here is where you backtrack****"


#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
#Note:
#
#The same word in the dictionary may be reused multiple times in the segmentation.
#You may assume the dictionary does not contain duplicate words.
#Example 1:
#
#Input: s = "leetcode", wordDict = ["leet", "code"]
#Output: true
#Explanation: Return true because "leetcode" can be segmented as "leet code".
#Example 2:
#
#Input: s = "applepenapple", wordDict = ["apple", "pen"]
#Output: true
#Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#             Note that you are allowed to reuse a dictionary word.
#Example 3:
#
#Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
#Output: false
class Approch2(object):
    def __init__(self, wordDict, s):
        self.wordDict = wordDict
        self.s = s

    def solution(self, i, sentence):
        if(i == len(self.s)):
            print sentence
            return True
        word = ""
        for index in range(i, len(self.s)):
            word = word+self.s[index]
            if(word in self.wordDict):
                if(self.solution(index+1, sentence+" "+word)):
                    return True
            

#Main Program
o = Approch1()
o.findAllOccourences("ilikesamsungmobile", "")
o.findFirstOccourence("ilikeicecreamandmango", "")
o2 = Approch2(["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango", "and"]
, "ilikeicecreamandmango")
print o2.solution(0, "")

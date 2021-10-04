# Number of Good Ways to Split a String
# https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

class Solution(object):
    def __init__(self):
        # key = (start index, end index) value = distinct character count
        self.tuplesOfDistinctChars = {}
    
    def addToDistinctAndCharCountHashSets(self, distinct, charCount, letter):
        # if we have not seen it
        if (letter not in charCount):
            charCount[letter] = 1
            distinct[letter] = True
            print "The character",letter,"is distinct and the distinct char count is",len(distinct)
        else:
            charCount[letter] = charCount[letter]+1
            print "The character",letter,"is not distinct and the distinct char count is",len(distinct)
    
    def distinctLeft(self, s):
        # count distinct from left to right
        # key = char, value = Number of times seen
        charCount = {}
        # key = char, value = True
        distinct = {}
        for i in range(len(s)):
            #print "For 0 to ",i,s[0:i+1]
            self.addToDistinctAndCharCountHashSets(distinct, charCount, s[i])
            self.tuplesOfDistinctChars[(0, i)] = len(distinct)
    
    def distinctRight(self, s):
        # count distinct from right to left
        # key = char, value = Number of times seen
        charCount = {}
        # key = char, value = True
        distinct = {}
        for i in range(len(s)-1, -1, -1):
            #print "For",len(s)-1,"to",i,"string",s[i:len(s)]
            self.addToDistinctAndCharCountHashSets(distinct, charCount, s[i])
            self.tuplesOfDistinctChars[(i, len(s)-1)] = len(distinct)
            
        
    def numSplits(self, s):
        self.distinctLeft(s)
        self.distinctRight(s)
        # split the string at various intervals and count good splits
        goodSplitCount = 0 
        for i in range(len(s)-1):
            print "First half", s[0:i+1],"Second half",s[i+1:len(s)]
            print "0 to",i,"and",i+1,"to",len(s)-1
            print "distinct in first half",self.tuplesOfDistinctChars[(0, i)]
            print "distinct in seconf half", self.tuplesOfDistinctChars[(i+1, len(s)-1)]
            if (self.tuplesOfDistinctChars[(0, i)] == self.tuplesOfDistinctChars[(i+1, len(s)-1)]):
                goodSplitCount = goodSplitCount + 1
            print "*"*25
        return goodSplitCount
        """
        :type s: str
        :rtype: int
        """
        

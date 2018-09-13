#Find All Anagrams in a String
#https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
class Approch1(object):
    def __init__(self):
        self.h = {}
        self.charCount = 0

    def insertInHash(self, pattern):
        for letter in pattern:
            if not(letter in self.h):
                self.h[letter] = 1
            else:
                self.h[letter] = self.h[letter]+1
        self.charCount = len(self.h)

    def addToHash(self, letter):
        if not (letter in self.h):
            return
        if(self.h[letter] == 0):
            self.charCount = self.charCount + 1
        self.h[letter] = self.h[letter]+1        
            
    def subFromHash(self, letter):
        if not (letter in self.h):
            return
        self.h[letter] = self.h[letter]-1
        if(self.h[letter] == 0):
            self.charCount = self.charCount -1

    def slidingWindow(self, string, pattern):
        output = []
        #start initial window
        for i in range(len(pattern)):
            self.subFromHash(string[i])
        #begin the algo
        window = 0
        stringIndex = len(pattern)-1
        while(stringIndex < len(string)):
            if(self.charCount == 0):
                output.append(window)
            self.addToHash(string[window])
            window = window+1
            stringIndex = stringIndex+1
            if(stringIndex < len(string)):
                self.subFromHash(string[stringIndex])
        print output
                
    def findAnagrams(self, string, pattern):
        if(len(string) < len(pattern)):
            return []
        self.insertInHash(pattern)
        self.slidingWindow(string, pattern)
        

#Main
o = Approch1()
o.findAnagrams("ccaebacbad", "abc")

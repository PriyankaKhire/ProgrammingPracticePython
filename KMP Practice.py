#KMP
#this is just me practicing kmp again
class KMP(object):
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern
        self.patternTable = [0 for i in range(len(pattern))]

    def fillPatternTable(self):
        i = 1
        j = 0
        while (i < len(self.pattern)):
            while(i < len(self.pattern) and self.pattern[i] == self.pattern[j]):
                self.patternTable[i] = j
                i = i+1
                j = j+1
            if(j == 0):
                i = i+1
            else:
                j = 0
        print self.patternTable

    def subStr(self):
        stringIndex = 0
        patternIndex = 0
        while(stringIndex < len(self.string)):
            while(stringIndex<len(self.string) and patternIndex < len(self.pattern) and self.string[stringIndex] == self.pattern[patternIndex]):
                stringIndex = stringIndex+1
                patternIndex = patternIndex+1
            if(patternIndex == len(self.pattern)):
                return stringIndex-1
            if(patternIndex == 0):
                stringIndex = stringIndex+1
            else:
                stringIndex = stringIndex-1
                patternIndex = patternIndex-1
                patternIndex = self.patternTable[patternIndex]
        return False
                
    def findSubString(self):
        self.fillPatternTable()
        print "Pattern found and ends at index ",  self.subStr(), " in the string"
        

#Main
o = KMP("abcxabcdabxabcdabcdabcy", "abcdabcy")
o.findSubString()

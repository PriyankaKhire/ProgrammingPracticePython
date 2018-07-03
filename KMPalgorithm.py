#Knuth-Morris-Pratt algorithm for string matching

class KMP(object):
    def __init__(self, string, pattern):
        self.string = string
        self.pattern = pattern

    #generate longest suffix which is same as suffix table for a Pattern
    def suffixTable(self):
        table = [0 for i in range(len(self.pattern))]
        prefix = 0
        suffix = prefix +1
        while (suffix < len(self.pattern)):
            if (self.pattern[prefix] == self.pattern[suffix]):
                #if pattern[suffix] == pattern[prefix] then
                table[suffix] = prefix + 1
                suffix = suffix+1
                prefix = prefix+1
            else:
                #if pattern[suffix] != pattern[prefix]
                while(prefix > 0 and self.pattern[prefix] != self.pattern[suffix]):
                    prefix = table[prefix-1]
                if(self.pattern[prefix] == self.pattern[suffix]):
                    table[suffix] = prefix + 1
                prefix = 0
                suffix = suffix + 1
        return table

    def patternMatch(self):
        patternTable = self.suffixTable()
        patternIndex = 0
        stringIndex = 0
        while(stringIndex < len(self.string) and patternIndex < len(self.pattern)):
            if(self.pattern[patternIndex] == self.string[stringIndex]):
                stringIndex = stringIndex + 1
                patternIndex = patternIndex + 1
            else:
                while(patternIndex > 0 and self.pattern[patternIndex] != self.string[stringIndex]):
                    patternIndex = patternTable[patternIndex-1]
                if(patternIndex == 0 and self.string[stringIndex] != self.pattern[patternIndex]):
                    stringIndex = stringIndex+1
        if(patternIndex == len(self.pattern)):
            #pattern found
            print "start index of pattern is "+str(stringIndex - len(self.pattern))
            return True
        print "pattern not found"
        return False
        


#Main Program
o = KMP("abcxabcdabxabcdabcdabcy", "xzsdflkjg")
print o.patternMatch()
        

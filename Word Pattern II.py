#Word Pattern II
#https://leetcode.com/problems/word-pattern-ii/
class Solution(object):

    def putInHash(self, pattern):
        patternHash = {}
        for char in pattern:
            if not(char in patternHash):
                patternHash[char] = True
        return patternHash

    #returns true if all values in hash table are assigned to some pattern in string
    def checkpatternHash(self, patternHash):
        for key in patternHash:
            if(patternHash[key] == True):
                return False
        return True

    def recurrse(self, pattern, string, patternIndex, stringIndex, patternHash, wordHash):
        print patternIndex, stringIndex, len(pattern), len(string), patternHash, wordHash
        if(patternIndex == len(pattern) and stringIndex == len(string)):
            if(self.checkpatternHash(patternHash)):
                return True
            else:
                return False
        if(patternHash[pattern[patternIndex]] != True):
            if(patternHash[pattern[patternIndex]] != string[stringIndex:stringIndex+len(patternHash[pattern[patternIndex]])]):
                return 
            else:
                self.recurrse(pattern, string, patternIndex+1, stringIndex+len(patternHash[pattern[patternIndex]]), patternHash, wordHash)
        for i in range(stringIndex, len(string)):
            if(string[stringIndex:i+1] in wordHash and wordHash[string[stringIndex:i+1]] != pattern[patternIndex]):
                continue
            patternHash[pattern[patternIndex]] = string[stringIndex:i+1]
            wordHash[string[stringIndex:i+1]] = pattern[patternIndex]
            if(self.recurrse(pattern, string, patternIndex+1, i+1, patternHash, wordHash)):
                return True
            #backtrack
            wordHash.pop(string[stringIndex:i+1], None)
            patternHash[pattern[patternIndex]] = string[stringIndex:i]
                
    def wordPatternMatch(self, pattern, str):
        if(pattern == str):
            return True
        if(pattern == "" or str == ""):
            return False
        patternHash = self.putInHash(pattern)
        if(self.recurrse(pattern, str, 0, 0, patternHash, {})):
            return True
        return False
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

class Solution2(object):
    def __init__(self):
        self.str = None
        self.pattern = None

    #We create a bijectional hash set such that key and value pair is unique.
    def logic(self, pi, si, hsPattern, hsStr):
        if(pi == len(self.pattern) and si < len(self.str)):
            return
        print "pattern Index ", pi, " string Index ", si, " pattern Hash ", hsPattern, " string hash ", hsStr
        if(pi == len(self.pattern) and si == len(self.str)):
            return True
        #if current pattern already found
        if(self.pattern[pi] in hsPattern):
            index = hsPattern.index(self.pattern[pi])
            string = hsStr[index]
            print "pattern Index ", pi, " string Index ", si, " String ", self.str[si:(si+len(string))], " hash string ", string
            if(string == self.str[si:(si+len(string))]):
                if( self.logic(pi+1, si + len(string), hsPattern, hsStr)):
                    return True
        #Assign current string letter to pattern
        i = si+1
        while(i < len(self.str)):
            if(self.str[si:i] in hsStr):
                return
            if((not (self.pattern[pi] in hsPattern)) and (not (self.str[si:i] in hsStr))):
                if(self.logic(pi+1, i, hsPattern+[self.pattern[pi]], hsStr+[self.str[si:i]])):
                    return True
            i = i+1

    def wordPatternMatch(self, pattern, str):
        print "String is ", str, " Pattern is ", pattern
        if(pattern == str):
            return True
        if(pattern == "" or str == ""):
            return False
        self.str = str
        self.pattern = pattern
        if( self.logic(0, 0, [], [])):
            return True
        return False
    
#Main
obj1 = Solution2()
#print obj1.wordPatternMatch('abab', 'redblueredblue')

obj2 = Solution2()
#print obj2.wordPatternMatch('aaaa', 'asdasdasdasd')

obj3 = Solution2()
#print obj3.wordPatternMatch('aabb', 'xyzabcxzyabc')

obj4 = Solution2()
#print obj4.wordPatternMatch('ab', 'aa')

obj5 = Solution2()
#print obj5.wordPatternMatch("itwasthebestoftimes", "ittwaastthhebesttoofttimes")

obj6 = Solution2()
#print obj6.wordPatternMatch('arora', 'aarrorraa')

obj7 = Solution2()
print obj7.wordPatternMatch("edcs", "electronicengineeringcomputerscience")

obj8 = Solution2()
#print obj8.wordPatternMatch("d", "ef")



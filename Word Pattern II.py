#Word Pattern II
#https://leetcode.com/problems/word-pattern-ii/
class Solution(object):
    #def __init__(self):

    def formPiTable(self, string):
        print string
        piTable = [0 for i in range(len(string))]
        index = 1
        startIndex = 0
        while(index < len(string)):
            if(string[index] == string[startIndex]):
                piTable[index] = startIndex + 1
                index = index + 1
                startIndex = startIndex + 1
            else:
                index = index + 1
                startIndex = 0
        print piTable

    def putInHash(self, pattern):
        hashTable = {}
        for char in pattern:
            if not(char in hashTable):
                hashTable[char] = True
        return hashTable

    def recurrse(self, pattern, string, patternIndex, stringIndex, hashTable):
        print patternIndex, stringIndex, len(pattern), len(string), hashTable
        if(patternIndex == len(pattern) or stringIndex == len(string)):
            print "finish"
            return
        print patternIndex
        if(hashTable[pattern[patternIndex]] != True):
            if(hashTable[pattern[patternIndex]] != string[stringIndex:stringIndex+len(hashTable[pattern[patternIndex]])]):
                return
            else:
                self.recurrse(pattern, string, patternIndex+1, stringIndex+len(hashTable[pattern[patternIndex]]), hashTable)
        for i in range(stringIndex, len(string)):
            hashTable[pattern[patternIndex]] = string[stringIndex:i+1]
            self.recurrse(pattern, string, patternIndex+1, i+1, hashTable)
            
            
                
                
    def wordPatternMatch(self, pattern, str):
        #self.formPiTable(pattern)
        #self.formPiTable(str)
        hashTable = self.putInHash(pattern)
        self.recurrse(pattern, str, 0, 0, hashTable)
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
#Main
obj1 = Solution()
obj1.wordPatternMatch('abab', 'redblueredblue')

obj2 = Solution()
#obj2.wordPatternMatch('aaaa', 'asdasdasdasd')

obj3 = Solution()
#obj3.wordPatternMatch('aabb', 'xyzabcxzyabc')

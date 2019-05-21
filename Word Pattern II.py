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
#Main
obj1 = Solution()
print obj1.wordPatternMatch('abab', 'redblueredblue')

obj2 = Solution()
print obj2.wordPatternMatch('aaaa', 'asdasdasdasd')

obj3 = Solution()
print obj3.wordPatternMatch('aabb', 'xyzabcxzyabc')

obj4 = Solution()
print obj4.wordPatternMatch('ab', 'aa')

obj5 = Solution()
print obj5.wordPatternMatch("itwasthebestoftimes", "ittwaastthhebesttoofttimes")

obj6 = Solution()
print obj6.wordPatternMatch('arora', 'aarrorraa')


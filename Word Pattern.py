#Word Pattern
#https://leetcode.com/problems/word-pattern/
class Solution(object):
    def __init__(self):
        #We create 2 saparate hash so the key is also unique to the value and vice versa, this is not possible with just 1 hash
        #since we want a bijenction between key and value we use 2 hash tables.
        self.patternToWordHash = {}
        self.wordToPatternHash = {}
        
    def putInHash(self, pattern, wordArray):
        patternIndex = 0
        wordIndex = 0
        while(patternIndex < len(pattern) and wordIndex < len(wordArray)):        
            if not(pattern[patternIndex] in self.patternToWordHash):
                if not(wordArray[wordIndex] in self.wordToPatternHash):
                    #map pattern letter to word
                    self.patternToWordHash[pattern[patternIndex]] = wordArray[wordIndex]
                    #map word to pattern
                    self.wordToPatternHash[wordArray[wordIndex]] = pattern[patternIndex]
            patternIndex = patternIndex + 1
            wordIndex = wordIndex + 1

    def compare(self, pattern, str):
        string = ""
        for char in pattern:
            if not(char in self.patternToWordHash):
                return False
            string = string + self.patternToWordHash[char] + " "
        if(string.strip() == str):
            return True
        return False

    def logic(self, pattern, str):
        self.putInHash(pattern, str.split(" "))
        return self.compare(pattern, str)
        
    def wordPattern(self, pattern, str):
        print self.logic(pattern, str)
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
#Main
obj1 = Solution()
obj1.wordPattern("he", "unit")

obj2 = Solution()
obj2.wordPattern("abba", "dog dog dog dog")

obj3 = Solution()
obj3.wordPattern("abba", "dog cat cat dog")

obj4 = Solution()
obj4.wordPattern("abba", "dog cat cat fish")

obj5 = Solution()
obj5.wordPattern("aaaa", "dog cat cat dog")

obj6 = Solution()
obj6.wordPattern("aaaa", "dog cat cat dog")

obj7 = Solution()
obj7.wordPattern("jquery", "jquery")

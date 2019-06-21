#Longest Repeating Character Replacement
#https://leetcode.com/problems/longest-repeating-character-replacement/
class LetterInfo(object):
    def __init__(self, letter, count, rangeStart):
        self.letter = letter
        self.count = count
        self.rangeStart = rangeStart
        self.rangeEnd = rangeStart
        self.span = 1
        self.differentLetters = 0
        
class Solution(object):
    def __init__(self):
        self.ht = {}
        self.maxCount = 0

    def getLetterRange(self, letterObj, s, k):
        mCount = 0
        windowStart = letterObj.rangeStart
        windowEnd = letterObj.rangeStart
        while(windowStart <= letterObj.rangeEnd and windowEnd <= letterObj.rangeEnd):            
            while(windowEnd <= letterObj.rangeEnd and ((s[windowEnd] == letterObj.letter) or (k > 0 and s[windowEnd] != letterObj.letter))):               
                if(s[windowEnd] != letterObj.letter):
                    k = k-1
                windowEnd = windowEnd+1                          
            if(k == 0):
                mCount = max(mCount, windowEnd-windowStart)
                while(windowStart <= letterObj.rangeEnd and s[windowStart] == letterObj.letter):
                    windowStart = windowStart+1
                while(windowStart <= letterObj.rangeEnd and windowStart < windowEnd and s[windowStart] != letterObj.letter):
                    windowStart = windowStart+1
                    k = k+1
        return mCount

    def findDifferentLettersInSpanOfALetter(self, k, s):
        for key in self.ht:
            if(self.ht[key].differentLetters < k):
                self.maxCount = max(self.maxCount, self.ht[key].count+k)
            else:
                letterRangeCount = self.getLetterRange(self.ht[key], s, k)
                self.maxCount = max(self.maxCount, letterRangeCount)
            
    def countLetterOccourences(self, s):
        for i in range(len(s)):
            if not(s[i] in self.ht):
                self.ht[s[i]] = LetterInfo(s[i], 1, i)
            else:                
                self.ht[s[i]].count = self.ht[s[i]].count+1
                self.ht[s[i]].rangeEnd = i                
                self.ht[s[i]].span = self.ht[s[i]].rangeEnd - self.ht[s[i]].rangeStart +1
                self.ht[s[i]].differentLetters = self.ht[s[i]].span - self.ht[s[i]].count
        
    def characterReplacement(self, s, k):
        if(len(s) < k):
            return len(s)
        self.countLetterOccourences(s)
        if(len(self.ht) == 1):
            return len(s)
        self.findDifferentLettersInSpanOfALetter(k, s)
        print self.maxCount
        """
        :type s: str
        :type k: int
        :rtype: int
        """

#Main
obj = Solution()
obj.characterReplacement('GEFAECEAGC', 4)

class Solution(object):
    def findInDict(self, s, wordDict):
        wordsFound = []
        word = ""
        for i in range(len(s)):
            word = word+s[i]
            if(word in wordDict):
                wordsFound.append(word)
        return wordsFound
    
    def logic(self, s, wordDict, output, mainOutput):
        if(s == ""):
            mainOutput.append(" ".join(output))
            return
        words = self.findInDict(s, wordDict)
        for w in words:
            self.logic(s[len(w):], wordDict, output+[w], mainOutput)
            
    def wordBreak(self, s, wordDict):
        mainOutput = []
        self.logic(s, wordDict, [], mainOutput)
        return mainOutput
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

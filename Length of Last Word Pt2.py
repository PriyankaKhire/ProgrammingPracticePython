# Length of Last Word
# https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def getLastWord(self, s):
        word = ""
        for i in range(len(s)):
            if (s[i] == " "):
                continue
            # if current is not a space and previous letter was a space or -1 then we have a new word starting
            if (i-1 < 0 or s[i-1] == " "):
                word = ""
            word += s[i]
        return word

    def lengthOfLastWord(self, s):
        lastWord = self.getLastWord(s)
        return len(lastWord)
        """
        :type s: str
        :rtype: int
        """
        

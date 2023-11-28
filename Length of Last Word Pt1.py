# Length of Last Word
# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        array = s.split(" ")
        for word in reversed(array):
            if (word):
                return len(word)
        """
        :type s: str
        :rtype: int
        """

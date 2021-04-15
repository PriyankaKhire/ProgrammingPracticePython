# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def isUnique(self, string):
        dupCount = []
        for s in string:
            if (s in dupCount):
                return False
            dupCount.append(s)
        return True
                
    def lengthOfLongestSubstring(self, s):
        if (self.isUnique(s)):
            return len(s)
        hashTable = {}
        start = 0
        end = 0
        length = 0
        # if string has duplicates
        for i in range(len(s)):
            end = i
            if(s[i] in hashTable):
                # if present then check if current index is in window
                if(hashTable[s[i]] >= start and hashTable[s[i]] <= end):
                    # get max length
                    length = max(length, end-start)
                    # restart
                    start = hashTable[s[i]]+1
            # update the index
            hashTable[s[i]] = i
        # we do check length of last string as well by checking for i+1-start
        # i+1 because i = len(string) and it doesn't give correct count. so we need to add one.
        return max(length, i+1-start)
        """
        :type s: str
        :rtype: int
        """
        

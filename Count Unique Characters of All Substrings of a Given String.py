# Count Unique Characters of All Substrings of a Given String
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

class Solution(object):
    def __init__(self):
        self.uniqueCount = 0
        
    def countUniqueChar(self, string):
        hashMap = {}
        for char in string:
            if char not in hashMap:
                hashMap[char] = 0
            hashMap[char] += 1
        # count the unique characters
        count = 0
        for key in hashMap:
            if (hashMap[key] == 1):
                count += 1
        return count
    
    def generateSubString(self, string):
        for start in range(0, len(string)):
            for end in range(start, len(string)+1):
                self.uniqueCount += self.countUniqueChar(string[start:end])
                
    def uniqueLetterString(self, s):
        self.generateSubString(s)
        return self.uniqueCount
        """
        :type s: str
        :rtype: int
        """
        

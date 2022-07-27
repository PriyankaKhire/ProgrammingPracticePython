# Valid Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def __init__(self):
        # key = letter, val = count
        self.hashMap = {}
    
    def addToMap(self, string):
        for letter in string:
            if (letter not in self.hashMap):
                self.hashMap[letter] = 1
            else:
                self.hashMap[letter] += 1
    
    def removeFromMap(self, string):
        for letter in string:
            if (letter not in self.hashMap):
                return False
            self.hashMap[letter] -= 1
            # if the count reaches 0 then remove that letter from hash map
            if (self.hashMap[letter] == 0):
                del self.hashMap[letter]
        return True
        
    def isAnagram(self, s, t):
        # add first string to hash map
        self.addToMap(s)
        # remove letter from map
        if not self.removeFromMap(t):
            return False
        # check if hash map still has letters
        if (self.hashMap):
            return False
        return True
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        

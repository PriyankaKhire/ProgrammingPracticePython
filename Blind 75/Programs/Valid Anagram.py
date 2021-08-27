# Valid Anagram
# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def putInHash(self, s):
        hashTable = {}
        for char in s:
            if (char not in hashTable):
                hashTable[char] = 0
            hashTable[char] = hashTable[char] + 1
        return hashTable
    
    def searchInHash(self, t, hashTable):
        # find the char in hash table.
        for char in t:
            if (char not in hashTable):
                return False
            hashTable[char] = hashTable[char] - 1
        # Make sure all count is zero in hash table
        for key in hashTable:
            if (hashTable[key] != 0):
                return False
        return True
                
    def isAnagram(self, s, t):
        hashTable = self.putInHash(s)
        return self.searchInHash(t, hashTable)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        

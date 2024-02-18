# Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def hashMapApproach(self, s, t):
        hashMap = {}
        # put s in hash map
        for letter in s:
            if (letter not in hashMap):
                hashMap[letter] = 0
            hashMap[letter] += 1
        # negate all letters in hash map for string t
        for letter in t:
            if (letter not in hashMap):
                return False
            hashMap[letter] -= 1
        # now see if hash map has any letter count not equal to 0
        for letter in hashMap:
            if (hashMap[letter] != 0):
                return False
        return True

    def sortingApproach(self, s, t):
        # sort s
        s = sorted(s)
        # sort t
        t = sorted(t)
        # compare the 2 lists
        if (s == t):
            return True
        return False

    def isAnagram(self, s, t):
        return self.sortingApproach(s, t)
        return self.hashMapApproach(s, t)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

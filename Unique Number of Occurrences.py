# Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/
class Solution(object):
    def uniqueOccurrences(self, arr):
        hashTable = {}
        # Put it in hash table
        for element in arr:
            if not element in hashTable:
                hashTable[element] = 0
            hashTable[element] = hashTable[element] + 1
        # count the occourances 
        occouranceSet = []
        for key in hashTable:
            occourence = hashTable[key]
            if occourence in occouranceSet:
                return False
            occouranceSet.append(occourence)
        return True
        """
        :type arr: List[int]
        :rtype:
